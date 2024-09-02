path = "CONTROLE DE EQUIPAMENTOS CALIBRÁVEIS.ods"
internal_table = "EQUIPAMENTOS CALIBRAÇÃO INTERNA"
external_table = "EQUIPAMENTOS CALIBRAÇÃO EXTERNA"
multimetro_folder = r"C:\Users\FELIPE\Documents\GitHub\OrganizadorPatrimonio\Planilhas\INTERNA\MULTÍMETRO"
display_volt_amp_folder = r"C:\Users\FELIPE\Documents\GitHub\OrganizadorPatrimonio\Planilhas\INTERNA\DISPLAY\DISPLAY VOLTÍMETRO AMPERÍMETRO"
display_volt_digt_folder = r"C:\Users\FELIPE\Documents\GitHub\OrganizadorPatrimonio\Planilhas\INTERNA\DISPLAY\DISPLAY VOLTIMETRO DIGITAL"
amperimetro_folder = r"C:\Users\FELIPE\Documents\GitHub\OrganizadorPatrimonio\Planilhas\INTERNA\ALICATE AMPERIMETRO"
sat_fa350_folder = r"C:\Users\FELIPE\Documents\GitHub\OrganizadorPatrimonio\Planilhas\INTERNA\JIGA - SAT - CARGA ELETRÔNICA\SAT\FA350ATE"
sat_fa4200_folder = r"C:\Users\FELIPE\Documents\GitHub\OrganizadorPatrimonio\Planilhas\INTERNA\JIGA - SAT - CARGA ELETRÔNICA\SAT\FA4200ATE"
sat_it8900_folder = r"C:\Users\FELIPE\Documents\GitHub\OrganizadorPatrimonio\Planilhas\INTERNA\JIGA - SAT - CARGA ELETRÔNICA\SAT\IT8900"
jiga_usb_folder = r"C:\Users\FELIPE\Documents\GitHub\OrganizadorPatrimonio\Planilhas\INTERNA\JIGA - SAT - CARGA ELETRÔNICA\JIGA USB"
jiga_g01158_folder = r"C:\Users\FELIPE\Documents\GitHub\OrganizadorPatrimonio\Planilhas\INTERNA\JIGA - SAT - CARGA ELETRÔNICA\JIGA G01158"
folder_name = r"\CERTIFICADO INTERNO DE CALIBRAÇÃO.ods"

# OS NOMES ABAIXO DEVEM ESTAR CONFORME A ABA EQUIPAMENTO DA PLANILHA
equipament_dic = {
    "Multímetro": (multimetro_folder, False),
    "DISPLAY VOLTÍMETRO AMPERÍMETRO": (display_volt_amp_folder, False),
    "DISPLAY VOLTÍMETRO DIGITAL": (display_volt_digt_folder, False),
    "Amperímetro": (amperimetro_folder, False),
    "SAT FA350": (sat_fa350_folder, False),
    "SAT FA4200": (sat_fa4200_folder, False),
    "SAT IT8900": (sat_it8900_folder, False),
    "JIGA USB": (jiga_usb_folder, False),
    "JIGA G01158": (jiga_g01158_folder, False)
}

patrimonys = {}