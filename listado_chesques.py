import csv
from msilib import datasizemask
import time

file = open("cheques.csv","r")

nombreArch = input(str("Ingrese cheques.csv"))
dni = input(str("Ingrese tu DNI"))
salida = input(str("Como quiere recibir la informacion? Pantalla o CSV"))
tipoDeCheque = input(str("Tipo de cheque: EMITIDO o DEPOSITADO"))
estadoDelCheque = input(str("Estado: PENDIENTE, APROBADO o RECHAZADO"))
fechaMinima = input(int("Ingrese fecha minima"))
fechaMaxima = input(int("Ingrese fecha maxima"))

def localizaPosiciones():
    archivoCreado = ""
    datosChequeNuevo = ""
    csv_reader = csv.DictReader(file, delimiter=',')
    for fila in csv_reader:
       if fila["DNI"]== dni:
        if fila["Tipo"]== tipoDeCheque:
            if fila["Estado"]== estadoDelCheque or estadoDelCheque == "":
                if fila["FechaPago"] > fechaMinima and fila["FechaPago"] < fechaMaxima:
                    if salida == "Pantalla":
                        print(fila)
                    elif salida == "CSV":
                        archivoCreado = dni + str(time.time()) + ".csv"
                        newArchivo = open(archivoCreado, "w")
                        datosChequeNuevo = fila["Valor"] + "," + fila["NumeroCuentaOrigen"]
                        newArchivo.write(datosChequeNuevo)
                    else:
                        print("Ingreso parametro incorrecto")

localizaPosiciones()

file.close()