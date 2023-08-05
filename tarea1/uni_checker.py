"""
J.E.V.A
02/08/23
funcion para graficar num de universidades por pais
version: 1.0.0
"""
import requests  # importamos la libreria requests


def uni_names():  # creamos la funcion para ver el nom de unis en x pais
    name = input("nombre del pais (en ingles): ")  # obtenemos el input del usuario
    req = requests.get(f"http://universities.hipolabs.com/search?country={name}")
    req_dic = req.json()  # convertimos de json a dic
    counter = 0
    print(f"las universidades de {name} son:\n")
    for i in req_dic:  # printeamos los nombres
        print(req_dic[counter]["name"])
        counter += 1
        i = i


def num_unis():  # funcion para ver num de unis en x pais
    name = input("nombre del pais (en ingles): ")  # obtenemos el input del usuario
    req = requests.get(f"http://universities.hipolabs.com/search?country={name}")
    req_dic = req.json()  # convertimos de json a dic
    counter = 0
    for i in req_dic:  # contamos las unis
        counter += 1
        i = i
    print(f"hay {counter} universidades en {name}")


def diff_num_unis():  # funcion para var difernecia del num de unis entre 2 paises
    name1 = input("nombre del pais1 (en ingles): ")  # obtenemos el input del usuario |
    name2 = input("nombre del pais2 (en ingles): ")  # |
    req1 = requests.get(f"http://universities.hipolabs.com/search?country={name1}")
    req1_dic = req1.json()  # convertimos de json a dic ||
    req2 = requests.get(f"http://universities.hipolabs.com/search?country={name2}")
    req2_dic = req2.json()  # ||
    counter1 = 0
    counter2 = 0
    for i in req1_dic:  # contamos las unis |||
        counter1 += 1
        i = i
    for i in req2_dic:  # |||
        counter2 += 1
        i = i
    if counter1 > counter2:  # hacemos la diferencia ||||
        print(f"{name1} tiene {counter1 - counter2} mas universidades que {name2}")
    elif counter2 > counter1:  # ||||
        print(f"{name2} tiene {counter2 - counter1} mas universidades que  {name1}")
    else:  # ||||
        print(f"{name1} y {name2} tienen la misma cantidad de univerisdades, {counter1}")
