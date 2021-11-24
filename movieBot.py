"""
Robo Telegram @mowvie_bot

robo especializado em realizar pesquisas de filmes no banco de dados
IMDB e apresentar a resposta traduzida para o português.
"""

import requests
from time import sleep
from my_token import TOKEN


class MovieBot:

    def __init__(self):
        TK = TOKEN
        self.url_base = f'https://api.telegram.org/bot{TK}/'
        self.result = self.url_base + 'getUpdates'
        self.info = ''

    def iniciar(self):
        while True:
            self.telegram_present()
            sleep(5)
            self.movie_api(self.telegram_last_message())
            if self.telegram_last_message() == 'sair':
                self.telegram_bye()
                sleep(1)
                break

    def telegram_result(self):
        update = self.result
        resp_json = requests.get(update)
        r = resp_json.json()
        return r['result']

    def telegram_last_message(self):
        result = self.telegram_result()
        lista_txt = []
        for i in range(len(result)):
            response = result[i]['message']
            for k, v in response.items():
                if k == 'text':
                    lista_txt.append(v)
        return lista_txt[-1]

    def telegram_chatID(self):
        result = self.telegram_result()
        id = result[-1]['message']['from']['id']
        return id

    def telegram_userName(self):
        result = self.telegram_result()
        user_name = result[-1]['message']['chat']['first_name']
        return user_name

    def telegram_present(self):
        id = self.telegram_chatID()
        presents = f'Olá bem vindo ao Movwie Bot {self.telegram_userName()}, eu sou um bot que faço pesquisa de títulos de filmes famosos ' \
                   '\nPara pesquisar basta digitar a palavra chave (em inglês)!\n Será muito divertido!'
        request = f'{self.url_base}sendMessage?chat_id={id}&text={presents}'
        requests.get(request)

    def telegram_bye(self):
        id = self.telegram_chatID()
        presents = f'Foi um prazer te atender {self.telegram_userName()}!\n Volte mais vezes!!!'
        request = f'{self.url_base}sendMessage?chat_id={id}&text={presents}'
        requests.get(request)

    def telegram_sendMessage(self, msg):
        id = self.telegram_chatID()
        request = f'{self.url_base}sendMessage?chat_id={id}&text={msg}'
        requests.get(request)

    def movie_api(self, msg):
        url = "https://imdb8.p.rapidapi.com/auto-complete"

        search_word = msg

        querystring = {"q": f"{search_word}"}

        headers = {
            'x-rapidapi-host': "imdb8.p.rapidapi.com",
            'x-rapidapi-key': "2270dbbd37mshba1996a088db08dp147312jsne1eeed53c98b"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        movie_dict = response.json()
        info = movie_dict['d']
        self.telegram_sendMessage(msg=f'Total de {len(info)} Filmes!!!! ')
        for i in range(len(info)):
            for k, v in info[i].items():
                if k == 'i':
                    self.telegram_sendMessage(msg=f"Poster  :  {v['imageUrl']}")
                elif k == 'l':
                    self.telegram_sendMessage(msg=f"Título :  {self.translate(v)}")
                elif k == 's':
                    self.telegram_sendMessage(msg=f"Atores : {v}")
                elif k == 'y':
                    self.telegram_sendMessage(msg=f"Ano : {v}")
                sleep(0.2)
            self.telegram_sendMessage(msg='---------------------------------------')
            self.telegram_sendMessage(msg="*Digite 'parar' para encerrar a pesquisa!")
            if self.telegram_last_message() == 'parar':
                break
        sleep(1)
        self.telegram_sendMessage(msg='Fim da listagem !!')
        sleep(1)
        self.telegram_sendMessage(msg='Digite <sair> para sair')

    def translate(self, palavra):
        url = "https://just-translated.p.rapidapi.com/"

        querystring = {"lang": "pt", "text": f"{palavra}"}

        headers = {
            'x-rapidapi-host': "just-translated.p.rapidapi.com",
            'x-rapidapi-key': "2270dbbd37mshba1996a088db08dp147312jsne1eeed53c98b"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        r = response.json()
        traduzido = r['text'][0]

        return traduzido


chat = MovieBot()
chat.iniciar()
