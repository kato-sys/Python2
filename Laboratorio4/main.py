"""
graficacion de datos utilizando Matplotlib
modificacion de archivo CSV utilizando pandas
J.E.V.A.
version: 1.0.0
"""
# importamos la librerias nececarias
import pandas as pd
import matplotlib.pyplot as plt

# nombraos la direccion del archivo
file = "/Users/johnevargasa/Documents/programing/Python/external data/ventas.csv"
ventas_datos = pd.read_csv(file)  # se convierte en data frame

# hacemos el calculo de las ganancias
ventas_datos["Ganancias"] = ventas_datos["Ventas"] - ventas_datos["Gastos"]
ventas_datos.to_csv(file, index=False, mode="w")  # se escribe en el archivo

plt.figure(figsize=(10, 10))  # le damos forma a la ventana
plt.xticks(fontsize=10, rotation=45)  # cambiamos las letras y su rotacion
# graficamos los datos y le damos nombres
plt.plot(ventas_datos["Mes"], ventas_datos["Ventas"], label="Ventas")
plt.plot(ventas_datos["Mes"], ventas_datos["Gastos"], label="Gastos")
# nombramos los ejes
plt.xlabel("Meses")
plt.ylabel("USD($)")
plt.legend()  # se crea la leyenda para ver los nombres
plt.show()  # se ensenya en la pantalla la grafica/leyenda
