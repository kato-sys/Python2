"""
J.E.V.A
02/08/23
funcion para graficar num de universidades por pais
version: 1.1.0
"""
import requests  # importamos la libreria requests
import pandas as pd
import matplotlib.pyplot as plt


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


def pais_num():
    global paises_dic  # nombramos una variable global
    print("ingrese los nombres de los paises separados por comma y espacio,")
    print("y en ingles. Por ejemplo: costa rica, united states: ")
    paises = input("ingresa los nombres aca: ")  # obtenemos el input
    paises_lista = paises.split(", ")
    paises_dic = {"pais": paises_lista}
    num_counter = []
    for i in paises_lista:  # se guardan los datos en un dicionario
        req1 = requests.get(f"http://universities.hipolabs.com/search?country={i}")
        req_dic = req1.json()  # convertimos de json a dic ||
        counter = 0
        for _ in req_dic:  # contamos las unis
            counter += 1
            _ = _
        num_counter.append(counter)
    paises_dic["universidades"] = num_counter


def uni_graph():
    pais_num()  # se llama la funcion para conseguir los datos
    paises_df = pd.DataFrame(paises_dic)  # se crean en un df
    print("Elija el tipo de grafica que quiere.")
    print("1: Pastel, 2: barras y 3: barra horizontal")
    grafico = input("Ingrese la opcion aqui: ")  # verificamos el input
    if grafico == "1":  # se crea y se enseña el codigo de paste
        plt.figure(figsize=(10, 10))
        plt.xticks(fontsize=10, rotation=45)
        plt.pie(paises_df["universidades"], labels=paises_df["pais"])
        plt.show()
    elif grafico == "2":  # se crea y se enseña el codigo de barras verticales
        x_axis = paises_dic["pais"]
        y_axis = paises_dic["universidades"]
        plt.figure(figsize=(10, 10))
        plt.xticks(fontsize=10, rotation=45)
        plt.bar(x_axis, y_axis)
        plt.xlabel("pais")
        plt.ylabel("numero de universidades")
        plt.show()
    elif grafico == "3":  # se crea y se enseña el codigo de barras horizontales
        x_axis = paises_dic["pais"]
        y_axis = paises_dic["universidades"]
        plt.figure(figsize=(10, 10))
        plt.xticks(fontsize=10, rotation=45)
        plt.barh(x_axis, y_axis)
        plt.xlabel("pais")
        plt.ylabel("numero de universidades")
        plt.show()
    else:  # se indica si hay una opcion invalida
        print("porfavor elejir una opcion valida.")
