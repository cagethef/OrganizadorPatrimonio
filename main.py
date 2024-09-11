""" 
-> PESSOA DIGITA O PATRIMONIO, PROGRAMA TEM QUE LER NA PLANILHA O 
EQUIPAMENTO E ABRIR A FICHA PRA PREENCHER MEDICOES;
-> QUANDO O USUARIO SALVAR A PLANILHA, TEM Q VERIFICAR O MODELO, PATRIMONIO, 
ERRO% E DATA;
-> SALVA O ARQUIVO NA PASTA CERTA DE ACORDO COM EQUIPAMENTO;
-> ENTRAR NA PASTA CALIBRACAO H:\DOCUMENTOS\CALIBRAÇÃO;
-> VERIFICAR NA PLANILHA SE É INTERNO/EXTERNO;
-> INTERNO -> PEGA NOME EQUIPAMENTO E SEU PATRIMONIO;
-> ENTRA NA PASTA Q TEM O NOME DO EQUIPAMENTO E VERIFICA SE TEM O 
DOCUMENTO DE CALIBRAÇÃO COM O PATRIMONIO;
-> CRIA PLANILHA DE FICHA DE CONTROLE INSTRUMENTOS COM BASE NOS DB E 
SE TIVER TUDO CERTO COM A PLANILHA GERA PDF NA PASTA DO EQUIPAMENTO;
-> NO EXTERNO VERIFICAR SE TEM MAIS DE UMA PAGINA NO PDF;
"""
import flet as ft
from app import App

window_size_height = 650   
window_size_width = 700

def main(page:ft.Page):
    page.window.height = window_size_height
    page.window.width = window_size_width
    page.window.max_height = window_size_height+5
    page.window.max_width = window_size_width+5
    page.window.min_height = window_size_height-5
    page.window.min_width = window_size_width-5
    page.theme_mode = "dark"
    page.title = "Pensar em um nome bala"
    page.add(App(page=page))

ft.app(main)