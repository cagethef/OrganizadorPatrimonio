import flet as ft

""" MINHAS BIBLIOTECAS """
from dataframe import *
import parameters
"""                    """
class App(ft.Container):
    """ Menu principal"""
    
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        

        self.patrimony_number = ft.TextField(
            label="Número de Patrimônio",
            input_filter=ft.NumbersOnlyInputFilter(),
            width=200,
            icon=ft.icons.ACCESSIBLE_FORWARD,tooltip="pq não usar?",
            autofocus=True,
            on_change=self.max_length,
            on_submit=self.search_equipament_with_patrimony_btn,
            
        )
        
        self.ok_button = ft.IconButton(
            tooltip="Procurar",
            icon=ft.icons.ADD,
            highlight_color=ft.colors.GREEN_400,
            on_click=self.search_equipament_with_patrimony_btn,
        )
        
        self.data_checkbox = ft.Checkbox(value=True,on_change=self.checkbox_changed, tristate=True)
        self.checkbox_text = ft.Text("Apenas encontrado.",width=200,size=15)
        
        self.data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Equipamento")),
                ft.DataColumn(ft.Text("Patrimonio")),
                ft.DataColumn(ft.Text("Status")),
            ]
        )
        
        self.content = self.create_tabs()
        
    def create_tabs(self):
        """Cria as abas. """
        return ft.Tabs(
        selected_index=0,
        animation_duration=300,
        divider_color=ft.colors.GREEN_400,
        tabs=[
            ft.Tab(
                text="Realizar Calibração",
                content = ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Divider(),
                            ft.Row(
                                controls=[
                                    self.patrimony_number,
                                    self.ok_button,
                                ],
                            ),
                            ft.Row(
                                controls=[
                                    ft.Text("teste"),
                                ],
                            ),
                        ],
                    )
                ),
            ),
            ft.Tab(
                text="Conferir Calibração",
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Divider(),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.FilledButton(
                                        text="Iniciar busca de documentos",
                                        on_click=self.search_documents,
                                    ),
                                ]
                            ),
                            ft.Row(
                                height=300,
                                #alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Column(
                                        width = 450,
                                        controls=[
                                            self.data_table,
                                        ],
                                    ),
                                    ft.Row(
                                        vertical_alignment=ft.CrossAxisAlignment.START,
                                        width = 400,
                                        height = 275,
                                        controls=[
                                            self.data_checkbox,
                                            self.checkbox_text,
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    )
                ),
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.SEARCH),
                content=ft.Text("Verificar multimetros"),
            ),
        ],
        expand=1,
    )
    
    def text_snack_bar(self,text,message_type):
        """ Define o estilo da snack bar com os seguintes parâmetros.
            text: Mensagem que irá aparecer na snack bar.
            message_type: Pode receber "erro" ou "ok" e irá mudar a cor do bg da snackbar.
        """
        
        if message_type == "erro":
            color = ft.colors.RED_400
        elif message_type == "ok":
            color = ft.colors.GREEN_ACCENT_400
            
        self.snack_bar = ft.SnackBar(
            content=ft.Text(
                value=text,
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.BLACK
                ),
            bgcolor=color
            )
        self.page.snack_bar = self.snack_bar
        self.page.snack_bar.open = True
        self.page.update()
            
    def max_length(self,e):
        value = e.control.value
        if(len(value) > 3):
            value = value[:3]
            e.control.value = value
        self.page.update()
        return
    
    def search_equipament_with_patrimony_btn(self,e):
        """ Pesquisa o num de patrimonio na planilha e retorna equip. """
        df = load_worksheet(parameters.path, parameters.internal_table)
        if df is not None:
            equipament = search_equipament_with_patrimony(df,
                            int(self.patrimony_number.value))
            if equipament:
                folder = equipament_open_folder(equipament)
                if folder:
                    self.text_snack_bar("Arquivo de calibração aberto","ok")
                else:
                    self.text_snack_bar("Arquivo de calibração não encontrado","erro")

            else:
                self.text_snack_bar("Nenhum equipamento com esse patrimonio.","erro")
        else:
            self.text_snack_bar("Erro ao carregar a planilha.","erro")
            
    def search_documents(self,e):
        patrimonys = {}
        df = load_worksheet(parameters.path, parameters.internal_table)
        for equip in parameters.my_equips:
            patrimonys[equip] = search_all_patrimony_from_equip(df,equip)
        for key in patrimonys.keys():
            # print(key)
            # print("\n")
            # print(patrimonys[key])
            # print("\n"*5)
            search_pdf(equipament_folder(key)+"\ATUAL",patrimonys[key])
        self.update_table()
    
    def update_table(self):
        status_filter = []
        data = [
            {"Equipamento": "Multimetro", "Patrimonio": "12345", "Status": "Encontrado"},
            {"Equipamento": "Display", "Patrimonio": "67890", "Status": "Não Encontrado"},
            {"Equipamento": "Alicate", "Patrimonio": "54321", "Status": "Encontrado"},
            {"Equipamento": "SAT", "Patrimonio": "09876", "Status": "Não Encontrado"},
        ]
        print(self.checkbox_text.value)
        if self.checkbox_text.value == "Apenas encontrado.":
            status_filter.append("Encontrado")
        elif self.checkbox_text.value == "Apenas não encontrado.":
            status_filter.append("Não Encontrado")
        else:
            status_filter.append("Todos")
        """
            "Todos" in status_filter: Se status_filter contém "Todos", 
            todos os itens serão incluídos, ignorando outros filtros.
            item["Status"] in status_filter: Se o filtro contém um status específico, 
            apenas itens com esse status serão incluídos.
            Portanto, se status_filter contiver "Todos", todos os itens serão incluídos, 
            independentemente do seu status. Se não contiver "Todos", 
            apenas itens cujo status está na lista status_filter serão incluídos.
            """
        filtered_data = [item for item in data if "Todos" in status_filter or item["Status"] in status_filter]
        self.data_table.rows = [ft.DataRow(cells=[
            ft.DataCell(ft.Text(item["Equipamento"])),
            ft.DataCell(ft.Text(item["Patrimonio"])),
            ft.DataCell(ft.Text(item["Status"])),
        ]) for item in filtered_data]
        self.page.update()

        
    def checkbox_changed(self,e):
        print(e.control.value)
        if e.control.value is True:
            self.checkbox_text.value = "Apenas encontrado."
        elif e.control.value is None:
            self.checkbox_text.value = "Apenas não encontrado."
        elif e.control.value is False:
            self.checkbox_text.value = "Todos os equipamentos."
        self.update_table()
        self.page.update()
        