"""
Modulo de funciones API para chucknorris.io
J.E.V.A.
28/07/23
version: 1.0.0
"""
# se importan librerias necesarias
import requests


def get_random():  # se crea la funcion para el chiste random
    req_random = requests.get(url="https://api.chucknorris.io/jokes/random")
    req_random_dic = req_random.json()
    print(req_random_dic['value'])


def get_categories():  # se crea la funcion para ver las categorias
    req_categories = requests.get(url="https://api.chucknorris.io/jokes/categories")
    req_categories_dic = req_categories.json()
    print(*req_categories_dic)


def get_specific(specify):  # se crea la funcion para elegir chistes especificos
    req_specific = requests.get(f"https://api.chucknorris.io/jokes/random?category={specify}")
    req_specific_dic = req_specific.json()
    print(req_specific_dic['value'])
