path = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\CONTROLE DE EQUIPAMENTOS CALIBRÁVEIS.ods"
internal_table = "EQUIPAMENTOS CALIBRAÇÃO INTERNA"
external_table = "EQUIPAMENTOS CALIBRAÇÃO EXTERNA"
multimetro_folder = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\MULTÍMETRO"
standard_multimetro_folder = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\EXTERNO\MULTÍMETRO PADRÃO"
display_volt_amp_folder = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\DISPLAY\DISPLAY VOLTÍMETRO AMPERÍMETRO"
display_volt_digt_folder = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\DISPLAY\DISPLAY VOLTIMETRO DIGITAL"
amperimetro_folder = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\ALICATE AMPERIMETRO"
standard_amperimetro_folder = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\EXTERNO\ALICATE AMPERÍMETRO PADRÃO"
dip_tester = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\EXTERNO\DIP TESTER"
paquimetro = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\EXTERNO\PAQUÍMETRO"
sat_fa350_folder = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\JIGA - SAT - CARGA ELETRÔNICA\SAT\FA350ATE"
sat_fa4200_folder = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\JIGA - SAT - CARGA ELETRÔNICA\SAT\FA4200ATE"
#sat_it8900_folder = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\JIGA - SAT - CARGA ELETRÔNICA\SAT\IT8900"
jiga_usb_folder = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\JIGA - SAT - CARGA ELETRÔNICA\JIGA USB"
jiga_g01158_folder = r"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\JIGA - SAT - CARGA ELETRÔNICA\JIGA G01158"
shunt_folder = r"H:\DOCUMENTOS\CALIBRAÇÃO\EXTERNO\RESISTOR SHUNT"
folder_name = r"\CERTIFICADO INTERNO DE CALIBRAÇÃO.ods"
ficha_pdf = r"FICHA DE CONTROLE DE INSTRUMENTOS.pdf"
ficha_path = r"\FICHA DE CONTROLE DE INSTRUMENTOS.ods"
# OS NOMES ABAIXO DEVEM ESTAR CONFORME A ABA EQUIPAMENTO DA PLANILHA
equipament_dic = {
    "Multímetro": (multimetro_folder, False),
    "Multímetro Padrão": (standard_multimetro_folder, False),
    "DISPLAY VOLTÍMETRO AMPERÍMETRO": (display_volt_amp_folder, False),
    "DISPLAY VOLTÍMETRO DIGITAL": (display_volt_digt_folder, False),
    "Amperímetro": (amperimetro_folder, False),
    "Amperímetro Padrão": (standard_amperimetro_folder, False),
    "Dip Tester": (dip_tester, False),
    "Paquímetro": (paquimetro, False),
    "SAT FA350": (sat_fa350_folder, False),
    "SAT FA4200": (sat_fa4200_folder, False),
    #"SAT IT8900": (sat_it8900_folder, False),
    "JIGA USB": (jiga_usb_folder, False),
    "JIGA G01158": (jiga_g01158_folder, False),
    "Resistor Shunt": (shunt_folder, False)
}

patrimonys = []