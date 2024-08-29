import pandas as pd
import numpy as np
import datetime

path = "CONTROLE DE EQUIPAMENTOS CALIBRÁVEIS.ods"


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
        print("Patrimonio não encontrado.")
        return None

def equipament_folder(equipament: str) -> str:
    """ Retorna a pasta onde deve alocar as informações do equipamento. """
    equipament_dic = {
    "Multímetro": "pasta tal",
    "DISPLAY VOLTÍMETRO AMPERÍMETRO": "pasta blau",
    "DISPLAY VOLTÍMETRO DIGITAL": "a",
    "Amperímetro": "b",
    "SAT": "c",
    "JIGA": "d"
    }
    return equipament_dic[equipament]

# "EQUIPAMENTOS CALIBRAÇÃO EXTERNA"
# "EQUIPAMENTOS CALIBRAÇÃO INTERNA"
my_table = "EQUIPAMENTOS CALIBRAÇÃO INTERNA"
df = load_worksheet(path, my_table)

if df is not None:
    patrimony = int(input("Digite o número de patrimonio: "))
    
    equipament = search_equipament_with_patrimony(df, patrimony)

    print(f"Busquei o patrimonio de número {patrimony} e o equipamento é um {equipament}")
    folder = equipament_folder(equipament)
    print(f"a pasta é {folder}")
    