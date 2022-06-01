import requests
import json
import src

token = "f696580631227c10d8b3f42d22b82817"
type_to = 1

data = src.Pegar_ip
id_city = ''

if type_to == 1:
    iCITY = data.city
    iURL = f'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={iCITY}&token={token}'
    iRESPONSE = requests.request('GET', iURL)
    iRETORNO = json.loads(iRESPONSE.text)
    for iCHAVE in iRETORNO:
        ID = iCHAVE['id']
        Cidade = iCHAVE['name']
        Estado = iCHAVE['state']
        Pais = iCHAVE['country']
        if iCITY == Cidade and data.state == Estado:
            id_city = ID
        print(f'ID: {ID}  Cidade: {Cidade}-{Estado}  País: {Pais}')
    iNEWCITY = id_city

    """
        'http://apiadvisor.climatempo.com.br/api-manager/user-token/:your-app-token/locales' \
                - H 'Content-Type: application/x-www-form-urlencoded' \
                - d 'localeId[]=3477'
        """

    iURL = f'http://apiadvisor.climatempo.com.br/api-manager/user-token/{token}/locales'
    payload = f"localeId[]={iNEWCITY}"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    iRESPONSE = requests.request("PUT", iURL, headers=headers, data=payload)
    type_to += 1

if type_to == 2:
    iURL = f"http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{iNEWCITY}/current?token={token}"
    iRESPONSE = requests.request("GET", iURL)
    iRETORNO = json.loads(iRESPONSE.text)
    data = iRETORNO['data']
    returno = {
        """'ID': iRETORNO['id'],"""
        'Name': iRETORNO['name'],
        'Estado': iRETORNO['state'],
        'Pais': iRETORNO['country'],
        'Dados': {
            'Condicao': data['condition'],
            'Temperatura': data['temperature'],
            'Sensacao termica': data['sensation']
        },
        'Data-Hora': data['date']
    }
