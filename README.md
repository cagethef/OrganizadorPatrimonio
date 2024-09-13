 ## **BEM VINDO AO PYTRIMÔNIO**

## INTRODUÇÃO
O software Pytrimônio foi projetado para conferir o processo de calibração de equipamentos elétricos. Seu principal objetivo é minimizar erros após a calibração, garantindo precisão e eficiência no controle dos documentos. A ferramenta oferece um ambiente intuitivo e de fácil uso, contribuindo para a redução de falhas humanas.

## **Instalação**

 Para instalar o Pytrimônio, siga estas etapas: 

1. Clone o repositório: **`https://github.com/cagethef/OrganizadorPatrimonio.git`** 
2. Navegue até o diretório do projeto: **`cd OrganizadorPatrimonio`** 
3. Instale as dependências: **`npm install`** 
4. Crie o projeto: **`npm run build`** 
5. Inicie o projeto: **`npm start`** 

## **Função das abas**

## **Conferir Calibração** 

1. A aba "Conferir Calibração" tem como objetivo auxiliar o usuário a identificar quais equipamentos estão ou não com seus arquivos salvos na sua respectiva pasta. Para o seu correto funcionamento é essencial a atualização correta da planilha CONTROLE DE EQUIPAMENTOS CALIBRÁVEIS.        
   
   1.1 **Iniciar busca de documentos**.
      Botão de ação que inicia o conferimento dos documentos de calibração.
      Após dar início a busca, os resultados serão mostrados pelas seguintes colunas.
      Equipamentos:
      Nesta coluna aparecerá todos os instrumentos calibráveis (de acordo com a planilha  CONTROLE DE EQUIPAMENTOS CALIBRÁVEIS).
      Patrimônio:
      Nesta coluna aparecerá o números do patrimônio dos instrumentos.
      Status:
      Nesta coluna aparecerá a situação que se encontra os instrumentos, variando de “Encontrado” para os instrumentos encontrados, e “Não Encontrado” para os instrumentos não encontrados.                  
  1.2 **Filtros**
      Há três possíveis filtros sendo eles: Ver todos os equipamentos, ver apenas os equipamentos encontrados, ver apenas equipamentos não encontrados.
## **Busca de Instrumentos**
2. **Busca de Instrumentos**           
   Essa aba consiste na busca de informações básicas do instrumento de acordo com o patrimônio digitado pelo usuário. Ele busca todas as informações da planilha CONTROLE DE EQUIPAMENTOS CALIBRÁVEIS sem precisar abrir.
## **Informações adicionais**
   Como funciona a verificação?
A verificação é feita pegando todos os patrimônios que estão na planilha de CONTROLE DE EQUIPAMENTOS CALIBRÁVEIS, isso inclui a aba de equipamentos internos e externos. Com esses patrimônios o programa separa pelo tipo de equipamento e em sua respectiva pasta busca se todos os patrimônios desse equipamento estão listados na FICHA DE CONTROLE DE INSTRUMENTOS. Se tudo estiver coerente, então ele entra na pasta ATUAL do equipamento e procura todos os pdf 's. Esses arquivos devem ser nomeados com o nº de patrimônio. 
Pastas verificadas:
As pastas verificadas são:

**Para equipamentos internos:**

	"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\MULTÍMETRO"
	"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\ALICATE AMPERIMETRO"
	"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\DISPLAY\DISPLAY VOLTÍMETRO AMPERÍMETRO"
	"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\DISPLAY\DISPLAY VOLTIMETRO DIGITAL"
	"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\JIGA - SAT - CARGA ELETRÔNICA\JIGA G01158"
	"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\JIGA - SAT - CARGA ELETRÔNICA\JIGA USB"
	"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\JIGA - SAT - CARGA ELETRÔNICA\SAT\FA350ATE"
	"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\INTERNA\JIGA - SAT - CARGA ELETRÔNICA\SAT\FA4200ATE"

**Para equipamentos externos:**

	"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\EXTERNO\MULTÍMETRO PADRÃO"
	"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\EXTERNO\ALICATE AMPERÍMETRO PADRÃO"
	"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\EXTERNO\PAQUÍMETRO"
	"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\EXTERNO\RESISTOR SHUNT"
	"\\servidor\desenv\DOCUMENTOS\CALIBRAÇÃO\EXTERNO\DIP TESTER"

Dentro dessas pastas são verificadas a pasta ATUAL e a FICHA DE CONTROLE DE INSTRUMENTOS.
 # **IMPORTANTE**
  O programa NÃO verifica o que está nos pdf 's, portanto, é função do gestor conferir e assinar eletronicamente.
  A planilha  CONTROLE DE EQUIPAMENTOS CALIBRÁVEIS deve sempre estar atualizada com as informações certas, pois é de lá que as informações são retiradas.
  É importante antes de iniciar uma calibração mover as calibrações anteriores para DESATUALIZADO com uma pasta do ano corrente.

Esse programa é feito para auxiliar na verificação de documentos. A responsabilidade da calibração, verificação e a assinatura é de responsabilidade do gestor definido no PO-GDS02.


     

