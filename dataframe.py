import pandas as pd
import numpy as np
import datetime
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
    return df[df["Equipamento"]==equipament]["Número de Patrimônio"].tolist()
    
def search_all_patrimony(df) -> list:
    return df["Número de Patrimônio"].tolist()

def equipament_folder(equipament: dict) -> str:
    """ Retorna a pasta onde deve alocar as informações do equipamento. """
    equipament_dic = {
    "Multímetro": parameters.multimetro_folder,
    "DISPLAY VOLTÍMETRO AMPERÍMETRO": parameters.display_volt_amp_folder,
    "DISPLAY VOLTÍMETRO DIGITAL": parameters.display_volt_digt_folder,
    "Amperímetro": parameters.amperimetro_folder,
    "SAT": parameters.sat_folder,
    "JIGA": parameters.jiga_folder
    }
    return equipament_dic.get(equipament)
          
def equipament_open_folder(equipament: str) -> str:
    """ Retorna a pasta onde deve alocar as informações do equipamento. """
    equipament_dic = {
    "Multímetro": parameters.multimetro_folder,
    "DISPLAY VOLTÍMETRO AMPERÍMETRO": parameters.display_volt_amp_folder,
    "DISPLAY VOLTÍMETRO DIGITAL": parameters.display_volt_digt_folder,
    "Amperímetro": parameters.amperimetro_folder,
    "SAT": parameters.sat_folder,
    "JIGA": parameters.jiga_folder
    }
    try:
        os.startfile(equipament_dic.get(equipament))
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
    print(df)

def search_pdf(path, patrimony_list):
    """ Pega a lista de patrimonios e verifica se existe pdf de todos. """
    print(path)
    for number in patrimony_list:
        pdf_name = f"{number}.pdf"
        pdf_path = os.path.join(path,pdf_name)
        
        if os.path.isfile(pdf_path):
            print(f"Arquivo {pdf_name} encontrado.")
        else:
            print(f"Arquivo {pdf_name} não encontrado.")
    

  
my_equip = "Multímetro"
df = load_worksheet(parameters.path, parameters.internal_table)
#result = search_all_patrimony_from_equip(df,my_equip)
#print(search_all_patrimony(df))
#search_pdf(parameters.multimetro_folder+"\ATUAL",result)
# patrimony = int(input("Digite o número de patrimonio: "))

# equipament = search_equipament_with_patrimony(df, patrimony)

# print(f"Busquei o patrimonio de número {patrimony} e o equipamento é um {equipament}")
# folder = equipament_folder(equipament)
#patrimony = 502
#load_calib_folder(parameters.display_volt_amp_folder+parameters.folder_name,patrimony)
    