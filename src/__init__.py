import requests
import json
from urllib.request import urlopen


class Pegar_ip:
    ip = str(requests.get('https://api.ipify.org/').text)
    if ip:
        iURL = f"http://ip-api.com/json/{ip}"

        request = urlopen(iURL)
        data = request.read().decode()

        data = eval(data)

        city = data['city']
        state = data['region']

    else:
        print('ERROR')
