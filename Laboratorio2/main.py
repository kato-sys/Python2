"""
J.E.V.A
Laboratorio concurrencia
13/07/23
version: 1.0.2
"""
# importamis las librerias necesarias
import api
import ids
import time
from concurrent.futures import ThreadPoolExecutor

input("presione 'enter' para comenzar con el normal/lento\n")
start = time.time()  # coemnzamos el reloj

for id in ids.ids:  # hacemos un simple loop para agarrar todos los id
    print(api.getOneUser(id)['name'])

# calculamos la diferencia en el tiempo para ver cuanto duro
end = time.time() - start
print(f"the function took {end:.2f}s to be completed.")

# ahora se vuelve hacer utilizando concurrencia
input("\npresione 'enter' para seguir con el rapido/concurrente\n")

# se vuelve a iniciar el reloj
start = time.time()


def getname(name):  # se crea una funcion para ver los nombres
    print(api.getOneUser(name)['name'])


# creamos una pool de threads y se llama la funcion en ellos
with ThreadPoolExecutor(max_workers=8) as exe:
    names = exe.map(getname, ids.ids)

end = time.time() - start  # se calcula el tiempo que paso
print(f"the function took {end:.2f}s to be completed.")
