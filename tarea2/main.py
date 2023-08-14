import uni_checker

# mensaje de bienvenida
print("Bienvenidos a uni-checker,")
print("aca podras averiguar cuales y cuantas universidades hay en un pais.")
while True:  # comenzamos el loop
    print("¿deseas conocer mas? y/n")
    yes_no = input("ingresa su opcion aca: ")  # preguntamos si quiere comenzar o salirse
    if yes_no == "y":  # si es si imprimimos las opciones
        print("¿que desea hacer?")
        print("1:imprimir los nombres de las universidades de un pais.")
        print("2:revisar el numero de univerisdades en un pais.")
        print("3:comparar el numero de universidades entre 2 paises.")
        print("4: elejir tipo de grafica para visualizar datos.")
        choice = input("ingresa su opcion aca: ")
        if choice == "1":  # hacemos la opcion elejida |
            uni_checker.uni_names()
        elif choice == "2":  # |
            uni_checker.num_unis()
        elif choice == "3":  # |
            uni_checker.diff_num_unis()
        elif choice == "4":  # |
            uni_checker.uni_graph()  # |
        else:  # si no elige una valida se le avisa ||
            print("porfavor elegir una opcionn valida.")
    elif yes_no == "n":  # si se quiere salir se sale del programa
        break
    else:  # ||
        print("porfavor elegir una opcionn valida.")
print("¡Espero verles de nuevo pronto!")  # mensaje de despedida
