import pandas as pd
import numpy as np
import parameters
import os

""" MINHAS BIBLIOTECAS """
import parameters
"""                    """
def load_worksheet(path: str,table: str):
    """ Carrega a aba especifica da planilha. """
    try:
        df = pd.read_excel(path, sheet_name = table, engine='odf')
        return df
    except Exception as e:
        print(f"Erro ao ler a aba: {e}")
        return None
    
def search_equipament_with_patrimony(df, patrimony: int) -> str:
    """ Busca o nome do equipamento com base no patrimonio. """
    equipament = df[df['Número de Patrimônio'] == patrimony]
    if not equipament.empty:
        return equipament['Equipamento'].values[0]
    else:
        return None

def search_all_patrimony_from_equip(df,equipament: str) -> list:
    """Busca todos os patrimonios da planilha. """
    try:
        filtered_df = df[df["Equipamento"]==equipament]["Número de Patrimônio"].tolist()
        if filtered_df.empty:
            df = load_worksheet(parameters.path, parameters.external_table)
            filtered_df = df[df["Equipamento"]==equipament]["Número de Patrimônio"].tolist()
        if not filtered_df.empty:
            return filtered_df
    except:
        return False
    
def search_patrimony_from_equip(df, equipament: str):    
    """ Busca cada um dos patrimonios do equipamento. """
    patrimonios = df[df["Equipamento"] == equipament][ "Número de Patrimônio"].astype('int')
    if patrimonios.empty:
        df = load_worksheet(parameters.path,parameters.external_table)
        patrimonios = df[df["Equipamento"] == equipament]["Número de Patrimônio"].astype('int')
    for patrimonio in patrimonios:
        yield patrimonio
    
def search_all_patrimony(df) -> list:
    return df["Número de Patrimônio"].tolist()

def equipament_folder(equipament: dict) -> str:
    """ Retorna a pasta onde deve alocar as informações do equipamento. """
    return parameters.equipament_dic.get(equipament)
          
def equipament_open_folder(equipament: str) -> str:
    """ Retorna a pasta sonde deve alocar as informações do equipamento. """
    try:
        os.startfile(parameters.equipament_dic.get(equipament))
        return True
    except:
        return None

def change_patrimony(text, patrimony):
    if text == "Número de Identificação: ":
        return f"Número de Identificação: {patrimony}"
    return text

def load_calib_folder(path: str, patrimony: int):
    df = pd.read_excel(path,engine='odf')
    df["Unnamed: 0"] = df["Unnamed: 0"].apply(lambda x: change_patrimony(x,patrimony))

def return_line_from_patrimony(patrimony):
    """ Retorna a linha inteira como uma lista com base no patrimonio. """
    df = load_worksheet(parameters.path,parameters.internal_table)
    try:
        filtered_df = df[df['Número de Patrimônio'] == patrimony]
        
        if filtered_df.empty:
            df = load_worksheet(parameters.path,parameters.external_table)
            filtered_df = df[df['Número de Patrimônio'] == patrimony]
        if not filtered_df.empty:
            return filtered_df.iloc[0].tolist()
    except:
        return False
    
    
    
def search_pdf(path, patrimony_list):
    """ Pega a lista de patrimonios e verifica se existe pdf de todos. """

    pdf_name = f"{patrimony_list}.pdf"
    pdf_path = os.path.join(path,pdf_name)
    if os.path.isfile(pdf_path):
        return "Encontrado."
    else:
        return "Não Encontrado."

def total_files_in_folder(path):
    """ Total de arquivos na pasta de calibraçao"""
    files = os.listdir(path)
    file_count = len(files)
    ficha_path = os.path.join(path, parameters.ficha_pdf)
    if os.path.isfile(ficha_path):
        file_count = file_count - 1
    else:
        return False
    # print(f"Equipamento: {equipament}")
    # print(f"Total patrimonios: {total_numbers}")
    # print(f"Na pasta: {file_count}")
    return True

def find_patrimony_ficha(path, patrimony):
    """ Busca os patrimonios na ficha individual. """
    try:
        if patrimony == 2:
            path = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\MULTÍMETRO"
        if patrimony == 600:
            path = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\ALICATE AMPERIMETRO"
        df = pd.read_excel(path+parameters.ficha_path, engine='odf', skiprows=5)
        filtered_df = df[df['IDENTIFICAÇÃO'] == patrimony]
        if filtered_df.empty:
            return print(f"Patrimonio não encontrado: {patrimony}")
        else:
            return None
    except:
        return True