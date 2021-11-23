"""
Este Arquivo tem como objetivo criar uma interface que seja capaz de
informar ao usuário sobre os valores de CriptoMoedas e suas variações
"""

import json
import PySimpleGUI as sg
import requests
from time import sleep
from datetime import date


class CriptosCoin:

    def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('Escolha o tipo de CriptoMoeda de Deseja Pesquisar')],
            [sg.Combo(["AAVE", "ACMFT", "ADA", "ALLFT", "AMFT", "ANKR", "ARGFT", "ASRFT", "ATMFT", "AXS",
                       "BAL", "BAND", "BARFT", "BAT", "BCH", "BNT", "BTC", "CRV", "DAL", "LTC", "MENGOFT",
                       "SCCPFT", "SNX", "UFCFT", "USDC"], size=(30, 10), key='coin')],
            [sg.Text('Escolha o Método que deseja Pesquisar')],
            [sg.Combo(["ticker", "day-summary"], size=(30, 10), key='method')],
            [sg.Button('Enviar'), sg.Button('Cancelar')],
            [sg.Output(size=(50, 25))]
        ]

        # janela
        self.janela = sg.Window('Pesquisa CriptoMoedas').layout(layout)

    def iniciar(self):
        while True:
            # extrair os dados da Tela

            self.button, self.values = self.janela.Read()
            if self.values['method'] == 'ticker':
                self.apresentar_resultado()
            elif self.values['method'] == 'day-summary':
                self.apresenta_diario()
            elif self.button == "Cancelar":
                sg.WIN_CLOSED
                self.window.close()
                break

    def pegar_api(self):
        base_url = f"https://www.mercadobitcoin.net/api/{self.values['coin']}/{self.values['method']}/"
        dados = requests.get(base_url)
        result = dados.text
        return result

    def apresentar_resultado(self):
        dados = self.pegar_api()
        resp = json.loads(dados)
        print(f"Pesquisando Resultados de {self.values['coin']} Mercado BitCoin ...")
        sleep(3)
        for k, v in resp.items():
            if self.values['method'] == 'ticker':
                for ik, iv in v.items():
                    sleep(0.5)
                    print(f"Tipo : {ik} : Valor : {iv}")

    def pega_diario_api(self):
        dia = str(date.today()).split('-')[2]
        dia = int(dia)
        dia -= 1
        dia = str(dia)
        mes = str(date.today()).split('-')[1]
        ano = str(date.today()).split('-')[0]
        base_url = f"https://www.mercadobitcoin.net/api/{self.values['coin']}/day-summary/{ano}/{mes}/{dia}/"
        get_api = requests.get(base_url)
        r = get_api.json()
        return r

    def apresenta_diario(self):
        dados = self.pega_diario_api()
        print(f"Pesquisando dados atualizados da cripto {self.values['coin']} do Mercado BitCoin ...")
        sleep(3)
        for k, v in dados.items():
            sleep(0.5)
            print(f" Tipo : {k}  ::  Valor :U$ {v}")


tela = CriptosCoin()
tela.iniciar()
