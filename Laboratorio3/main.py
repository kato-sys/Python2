"""
programa 'Main' para obtener y printear chistes de chuck norris.
J.E.V.A.
28/07/23
version: 1.0.0
"""
# importamos el modulo de funciones
import requests_chuck

# imprimimos un mensaje de bienvenida
print("this is the chuck norris museum, you're currently in the joke section")
print("what would you like to do?")

# coemnzamos el loop
while True:
    print("press 'y' to face chuck or 'n' to coward away")  # preguntamos si desea seguir
    on_off = input("")  # tomamos la decicion
    if on_off == "y":  # evualamos si sí para imprimir las opciones
        print("choose 1 for a random joke,")
        print("choose 2 to check the categories,")
        print("and lastly, choose 3 to ask for a specific category of joke.")
        choice = input("insert option here: ")
        if choice == "1":  # se obtiene el chiste
            requests_chuck.get_random()
        elif choice == "2":  # se enseñan las opciones
            requests_chuck.get_categories()
        elif choice == "3":  # se obtiene el chiste especifico
            specify = input("choose the category: ")
            requests_chuck.get_specific(specify)
        else:
            print("please choose a valid option.")
    elif on_off == "n":  # si no, se sale del loop
        break
    else:  # se revisa por opcion invalida
        print("please choose a valid option.")
# se printean mensaje de despedida
print("you may run from chuck norris, but you cant hide")
print("chuck noris will be awaiting your return.")
