"""
Módulo para recuperação de dados climáticos do PCBr.

    A documentação do Projeto pode ser encontrada no Portal
          http://pclima.inpe.br/
     
    As escolhas para o download de dados são definidas através 
     de um JSON que pode ser gerado utilizando do Portal API.
          http://pclima.inpe.br/analise/API
 
    versão do Python em que foi testada: 3.6
     
    exemplo de uso da API

    Token: consultar a documentação para a geração do Token

    import api as api

    Client = api.Client()

    data = Client.getData(
    { "formato": "CSV", "conjunto": "PR0002", "modelo": "MO0003", "experimento": "EX0003", "periodo": "PE0000", "cenario": "CE0001", "variavel": "VR0001", "frequenciaURL": "Mensal", "frequencia": "FR0003", "produto": "PDT0001", "localizacao": "Ponto", "localizacao_pontos": "-23.56/-46.62", "varCDO": "tasmax" }
    )

    Client.save(data,"file.csv")  
     
"""

import os
import json
from pclima.factory import RequestFactory

class Client(object):
    """
    Classe utilizada para criar um Cliente de acesso a API.

    Attributes
    ----------
    token : str
        Definido no arquivo ~/.pclimaAPIrc
    format : str
        Definido quando deseja um download


    """
    def __init__(self, token=os.environ.get("API_TOKEN"),):
        """
        Parameters
        ----------
        token : str
            Chave de acesso aos serviços da API

        """
        self.token = token
        self.format = None

        dotrc = os.environ.get("PCLIMAAPI_RC", os.path.expanduser("~/.pclimaAPIrc"))

        if token is None:
            if os.path.exists(dotrc):
                config = read_config(dotrc)

                if token is None:
                    token = config.get("token")

        if token is None:
            print("Missing/incomplete configuration file: %s" % (dotrc))
            raise SystemExit
            
        self.token = token


    def getData(self,apiJSON):
        """
        Method
        -------
        O Método envia o JSON e retorna os dados desejados.  

        Parameters
        ----------
        apiJSON : json
            JSON com as opções escolhidas

        Returns
        -------
        retorno depende do formato escolhido:
        
        Formato             Retorno:
        NetCDF              XArray
        CSV                 DataFrame
        JSON                DataFrame
        CSVPontos           DataFrame
        CSVPontosTransposta DataFrame 
        """
       
        j = json.loads(json.dumps(apiJSON))

        print(j)
        self.format = j["formato"]

        factory = RequestFactory()
        product = factory.get_order(j["formato"],self.token,j)
        print(product)
        return (product.download())

    def save(self,content,file):
        """
        Method
        -------
        O Método decebe a recuperacao do dado e o nome do arquivo
        se saída.

        Parameters
        ----------
        content : formato desejado
            Dados recuperados

        file : nome do arquivo de saída
            Nome do arquivo de saída Ex.: "saida.csv"
        """
        factory = RequestFactory()
        factory.save(self.format,content,file)

def read_config(path):
    config = {}
    with open(path) as f:
        for l in f.readlines():
            if ":" in l:
                k, v = l.strip().split(":", 1)
                if k in ("token"):
                    config[k] = v.strip()
    return config
