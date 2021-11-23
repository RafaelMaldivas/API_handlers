import datetime
import json
from time import sleep
import requests
"""dicionario_cript = [{"AAVE": "Aave",
                     "ACMFT": "Fan Token ASR",
                     "ADA": "Cardano",
                     "ALLFT": "BARFT",
                     "AMFT": "BARFT",
                     "ANKR": "ANKR",
                     "ARGFT": "BARFT",
                     "ASRFT": "Fan Token ASR",
                     "ATMFT": "Fan Token ATM",
                     "AXS": "Axie Infinity Shard",
                     "BAL": "Balancer",
                     "BAND": "Band Protocol",
                     "BARFT": "BARFT",
                     "BAT": "Basic",
                     "BCH": "Bitcoin",
                     "BNT": "BANCOR",
                     "BTC": "Bitcoin",
                     "CAIFT": "Fan",
                     "CHZ": "Chiliz",
                     "CITYFT": "BARFT",
                     "COMP": "Compound",
                     "CRV": "Curve",
                     "DAI": "Dai",
                     "DAL": "Balancer",
                     "LTC": "Litecoin",
                     "MCO2": "MCO2",
                     "MENGOFT": "Flamengo",
                     "SCCPFT": "Corinthians",
                     "SNX": "Synthetix",
                     "UFCFT": "UFC",
                     "USDC": "USD Coin"}]

values=[k.keys() for k in dicionario_cript]
print(values)
dia = str(datetime.date.today()).split('-')[2]
dia = int(dia)
dia -= 1
dia = str(dia)
mes = str(datetime.date.today()).split('-')[1]
ano = str(datetime.date.today()).split('-')[0]
print(dia, mes, ano)


def pega_diario_api(dia, mes, ano):

    base_url = f"https://www.mercadobitcoin.net/api/BTC/day-summary/{ano}/{mes}/{dia}/"
    get_api = requests.get(base_url)
    r = get_api.json()
    print(type(r))
    return r

print(pega_diario_api(dia, mes, ano))"""
'''
import requests

url = "https://imdb8.p.rapidapi.com/auto-complete"

search_word = "crazy"

querystring = {"q":f"{search_word}"}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "2270dbbd37mshba1996a088db08dp147312jsne1eeed53c98b"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
movie_dict = response.json()
print(movie_dict)
info = movie_dict['d']
for i in range(len(info)):
    for k, v in info[i].items():

        if k == 'i':
            print(f"Poster  :  {v['imageUrl']}")
        elif k == 'l':
            print(f'Título :  {v}')
        elif k == 's':
            print(f'Atores : {v}')
        elif k == 'y':
            print(f'Ano : {v}')
        sleep(1)

print(info)'''
'''while True:
    TOKEN = '2139915866:AAFV5S-kl61kd4jE7c-Bm-89_2aNd5-Yjmw'
    url_base = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    resp_json = requests.get(url_base)
    resp_dict = resp_json.json()
    result = resp_dict['result']
    mgs = result['message']

    print(result)
    sleep(8)'''


from googletrans import Translator
texto = 'bandeira'
tradutor = Translator()
traduz = tradutor.translate(texto)
print(traduz)
