
# PClima API

# NAME
    PClima API - Módulo para recuperação de dados climáticos do PCBr.

# DESCRIPTION
        A documentação do Projeto pode ser encontrada no Portal
              http://pclima.inpe.br/
         
        As escolhas para o download de dados são definidas através 
         de um JSON que pode ser gerado utilizando do Portal API.
              http://pclima.inpe.br/analise/API
     
        versão do Python em que foi testada: 3.6
         
        exemplo de uso da API
    
        Token: consultar a documentação para a geração do Token
        Em Windows colocar o arquivo .pclimaAPIrc no diretório inicial do usuário (ex. C:\User\Cliente)

        import pclima as pcl
    
        Client = pcl.Client()
    
        data = Client.getData(
        { "formato": "CSV", "conjunto": "PR0002", "modelo": "MO0003", "experimento": "EX0003", "periodo": "PE0000", "cenario": "CE0001", "variavel": "VR0001", "frequenciaURL": "Mensal", "frequencia": "FR0003", "produto": "PDT0001", "localizacao": "Ponto", "localizacao_pontos": "-23.56/-46.62", "varCDO": "tasmax" }
        )
    
        Client.save(data,"file.csv")

## CLASSES
    builtins.object
        Client
    
    class Client(builtins.object)
     |  Classe utilizada para criar um Cliente de acesso a API.
     |  
     |  Attributes
     |  ----------
     |  token : str
     |      Definido no arquivo ~/.pclimaAPIrc
     |  format : str
     |      Definido quando deseja um download
     |  
     |  Methods defined here:
     |  
     |  __init__(self, token=None)
     |      Parameters
     |      ----------
     |      token : str
     |          Chave de acesso aos serviços da API
     |  
     |  getData(self, apiJSON)
     |      Method
     |      -------
     |      O Método envia o JSON e retorna os dados desejados.  
     |      
     |      Parameters
     |      ----------
     |      apiJSON : json
     |          JSON com as opções escolhidas
     |      
     |      Returns
     |      -------
     |      retorno depende do formato escolhido:
     |      
     |      Formato             Retorno:
     |      NetCDF              XArray
     |      CSV                 DataFrame
     |      JSON                DataFrame
     |      CSVPontos           DataFrame
     |      CSVPontosTransposta DataFrame
     |  
     |  save(self, content, file)
     |      Method
     |      -------
     |      O Método decebe a recuperacao do dado e o nome do arquivo
     |      se saída.
     |      
     |      Parameters
     |      ----------
     |      content : formato desejado
     |          Dados recuperados
     |      
     |      file : nome do arquivo de saída
     |          Nome do arquivo de saída Ex.: "saida.csv"
     |  
     | 




