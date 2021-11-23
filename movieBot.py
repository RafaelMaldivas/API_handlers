"""
Robo Telegram @mowvie_bot

robo especializado em realizar pesquisas de filmes no banco de dados
IMDB e apresentar a resposta traduzida para o português.
"""

import requests
from time import sleep
from my_token import TOKEN


class MovieBot:


    def telegram_api(self):
        TK = TOKEN
        url_base = f'https://api.telegram.org/bot{TK}/getUpdates'
        resp_json = requests.get(url_base)
        r = resp_json.json()
        for i in range(len(r['result'])):
            result = r['result'][i]['message']
            for k, v in result.items():
                print(f'{k} : {v}')
                sleep(1)
            print()




    def movie_api(self, nome):

        url = "https://imdb8.p.rapidapi.com/auto-complete"

        search_word = nome

        querystring = {"q": f"{search_word}"}

        headers = {
            'x-rapidapi-host': "imdb8.p.rapidapi.com",
            'x-rapidapi-key': "2270dbbd37mshba1996a088db08dp147312jsne1eeed53c98b"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        movie_dict = response.json()
        info = movie_dict['d']
        for i in range(len(info)):
            for k, v in info[i].items():
                if k == 'i':
                    print(f"Poster  :  {v['imageUrl']}")
                elif k == 'l':
                    print(f'Título :  {self.translate(v)}')
                elif k == 's':
                    print(f'Atores : {v}')
                elif k == 'y':
                    print(f'Ano : {v}')
                sleep(0.5)
            print()

    def translate(self, palavra):

        url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
        word = palavra
        payload = f"q={word}&target=pt&source=en"
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'accept-encoding': "application/gzip",
            'x-rapidapi-host': "google-translate1.p.rapidapi.com",
            'x-rapidapi-key': "6b3493419bmshd7d193f5a4a3e43p1380f8jsn0e2983568b0b"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        r = response.json()
        r = r['data']['translations']
        texto = r[0]['translatedText']

        return texto




bot = MovieBot()
while True:
    bot.telegram_api()
    sleep(8)
    bot.movie_api('adventure')