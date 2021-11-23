"""
Created on Thu Nov 9/2021
@author: Rafael Maldivas
Estudo do Json
"""

import json

# abaixo temos uma string
json_string = '{"first_name": "Rafael", "last_name": "Silva"}'

# transformaremos a string json em dict
json_dict = json.loads(json_string)

print(json_dict.keys())  # acessando chaves
print(json_dict.items())  # acessando os items
print(json_dict.values())  # acessando os valores

# um exemplo de dicionário

filme = {
    "titulo": 'Clube da Luta',
    "duracao": 198,
    "ano": 1999,
    "atores": ['Brad Pitt', 'Edward Norton']
}

def formata_tipo_json(dict):
    '''
    função para tranformar dicionários em arquivos JSON
    :param dict:
    :return: arquivo formato JSON
    '''
    dump = json.dumps(dict)
    return dump

def formata_tipo_dict(json):
    '''
    função para transformar arquivo JSON em Dicionários
    :param json:
    :return: dicionário
    '''
    json_dict = json.loads(json)
    return json_dict


