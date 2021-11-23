import json

import PySimpleGUI as sg
import requests
from time import sleep


class BuscaCEP:

    def __init__(self):
        # layout
        layout = [
            [sg.Text('Digite o CEP', size=(9, 0)), sg.Input(key='cep', size=(0,8))],
            [sg.Text('Digite o número do endereço'), sg.Input(key='numero', size=(0,10))],
            [sg.Button('Enviar'), sg.Cancel()],
            [sg.Output(size=(35, 30))]
        ]
        # janela
        self.window = sg.Window('Pesquisa CEP').layout(layout)

    def iniciar(self):
        while True:
            # extrair os dados da Tela

            self.button, self.values = self.window.Read()

            if self.button == "Cancel":
                sg.WIN_CLOSED
                self.window.close()
                break

            elif len(self.values['cep']) == 8:
                self.cep = self.values['cep']
                self.retorna_enderço()

            else:
                print('Insira o cep corretamente')

    def pegar_cep(self):
        url = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/')
        return url.text

    def retorna_enderço(self):
        resp = self.pegar_cep()
        dados = json.loads(resp)
        print('Obtendo informações da API ....')
        for k, v in dados.items():
            if k == 'ibge':
                break
            sleep(1)
            print(f'{k} : {v}')
            if k == 'logradouro':
                print(f"Número : {self.values['numero']}")



tela = BuscaCEP()
tela.iniciar()

filme = {
    "title": "Star Wars",
    "gender": "Sci-fi",
    "duration": "228",
    "director": "Geoge Lucas",
    "main-actor": ["Mark Hammil", "Harison Ford", "C3PO"],
    "year": "1974"
}

apifilme = json.dumps(filme)
url_base = 'https://'
print(type(apifilme))