import flet as ft
import time
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
        
        self.search_patrimony_number = ft.TextField(
            label="Número de Patrimônio",
            input_filter=ft.NumbersOnlyInputFilter(),
            width=200,
            icon=ft.icons.PARAGLIDING,
            autofocus=True,
            on_change=self.max_length,
            on_submit=self.search_patrimony_infos,
            
        )
        
        self.search_ok_button = ft.IconButton(
            tooltip="Procurar",
            icon=ft.icons.SAVED_SEARCH,
            highlight_color=ft.colors.GREEN_400,
            on_click=self.search_patrimony_infos,
        )
        
        self.data_checkbox = ft.Checkbox(value=True,on_change=self.checkbox_changed, tristate=True)
        self.checkbox_text = ft.Text("Apenas encontrado.",width=200,size=15)
        self.equipament_text = ft.Text("",size=20)
        self.setor_text = ft.Text("",size=20)
        self.info_text = ft.Text("",size=20)
        self.date_text = ft.Text("",size=20)
        self.total_equip = ft.Text("",size=15,width=190,text_align=ft.TextAlign.RIGHT)
        
        self.loading_progress = ft.ProgressRing(width=30, height=30, stroke_width=3,value=0)
        
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
            # ft.Tab(
            #     text="Realizar Calibração",
            #     content = ft.Container(
            #         content=ft.Column(
            #             controls=[
            #                 ft.Divider(),
            #                 ft.Row(
            #                     controls=[
            #                         self.patrimony_number,
            #                         self.ok_button,
            #                     ],
            #                 ),
            #                 ft.Row(
            #                     controls=[
            #                         ft.Text("teste"),
            #                     ],
            #                 ),
            #             ],
            #         )
            #     ),
            # ),
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
                                    
                                    ft.Column(
                                        controls=[
                                            self.total_equip,
                                        ],
                                    ),
                                ]
                            ),
                            ft.Row(
                                height=580,
                                vertical_alignment=ft.CrossAxisAlignment.START,
                                controls=[
                                    ft.Column(
                                        scroll=ft.ScrollMode.HIDDEN,
                                        width = 450,
                                        height = 450,
                                        controls=[
                                            self.data_table,
                                            ft.Column(
                                                width = 400,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    self.loading_progress,
                                                ],
                                            ),
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
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Divider(),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text("Busca de instrumentos.",size=20)
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    self.search_patrimony_number,
                                    self.search_ok_button,
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.icons.RADIO),
                                    ft.Text("Equipamento:",size=20),
                                    self.equipament_text,
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.icons.ADD_LOCATION),
                                    ft.Text("Setor:",size=20),
                                    self.setor_text,
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.icons.INFO),
                                    ft.Text("Modelo:",size=20),
                                    self.info_text,
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.icons.CALENDAR_MONTH),
                                    ft.Text("Data prox calibração:",size=20),
                                    self.date_text,
                                ]
                            ),
                        ],
                    )
                ),
            ),
        ],
        expand=1,
    )
    
    def text_snack_bar(self, text, message_type):
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
            show_close_icon=True,
            close_icon_color=ft.colors.WHITE,
            bgcolor=color,
            duration=30000,
            )
        self.page.snack_bar = self.snack_bar
        self.page.snack_bar.open = True
        self.page.update()
            
    def max_length(self, e):
        value = e.control.value
        if(len(value) > 3):
            value = value[:3]
            e.control.value = value
        self.page.update()
        return
    
    def search_equipament_with_patrimony_btn(self, e):
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
            
    def search_documents(self, e):
        parameters.patrimonys = []
        self.update_table()
        self.total_equip.value = ""
        equip_sem_ficha = []
        error = False
        total_equip = 0
        df = load_worksheet(parameters.path, parameters.internal_table)
        for equip in parameters.equipament_dic.keys():
            generator = search_patrimony_from_equip(df,equip)
            cont = 0
            for patrimony in generator:
                self.loading_progress.value += 0.02
                self.page.update()
                if equipament_folder(equip) == None:
                    self.text_snack_bar(f"Equipamento {equip} não encontrado.","erro")
                    
                error = find_patrimony_ficha(equipament_folder(equip)[0],patrimony)
                if error:
                    self.text_snack_bar(f"FICHA DE CONTROLE DE INSTRUMENTOS FALTANDO EM {equip}", "erro")
                    return
                result = search_pdf(equipament_folder(equip)[0]+"\ATUAL",patrimony)
                parameters.patrimonys.append([equip, patrimony, result])
                cont += 1
                total_equip = total_equip+1
            if not total_files_in_folder(equipament_folder(equip)[0]+"\ATUAL"):
                equip_sem_ficha.append(equip)
                error = True
        if error:
            self.text_snack_bar(f"FICHA DE CONTROLE DE INSTRUMENTOS FALTANDO EM {equip_sem_ficha}", "erro")
            return
        self.total_equip.value = f"Total de Equipamentos: {total_equip}"
        self.loading_progress.value = 0
        self.update_table()
    
    def update_table(self):
        status_filter = []
        if self.checkbox_text.value == "Apenas encontrado.":
            status_filter.append("Encontrado.")
        elif self.checkbox_text.value == "Apenas não encontrado.":
            status_filter.append("Não Encontrado.")
        else:
            status_filter.append("Todos")
        
        filtered_data = [
            {"Equipamento": equip, "Patrimonio": patrimony, "Status": status}
            for equip, patrimony, status in parameters.patrimonys         
            if "Todos" in status_filter or status in status_filter
        ]
        self.data_table.rows = [ft.DataRow(cells=[
            ft.DataCell(ft.Text(item["Equipamento"])),
            ft.DataCell(ft.Text(item["Patrimonio"])),
            ft.DataCell(ft.Text(item["Status"])),
        ]) for item in filtered_data]
        self.page.update()

        
    def checkbox_changed(self, e):
        if e.control.value is True:
            self.checkbox_text.value = "Apenas encontrado."
        elif e.control.value is None:
            self.checkbox_text.value = "Apenas não encontrado."
        elif e.control.value is False:
            self.checkbox_text.value = "Todos os equipamentos."
        self.update_table()
        self.page.update()
        
    def search_patrimony_infos(self,e):
        patrimony = int(self.search_patrimony_number.value)
        try:
            row_list = return_line_from_patrimony(patrimony)
            self.equipament_text.value = row_list[0]
            self.setor_text.value = row_list[2]
            self.info_text.value = row_list[3]
            self.date_text.value = row_list[4].strftime("%d-%m-%Y")
        except:
            self.equipament_text.value = ""
            self.setor_text.value = ""
            self.info_text.value = ""
            self.date_text.value = ""
        self.page.update()
