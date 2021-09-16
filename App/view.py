"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
from time import process_time

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    
    
    print("1- Seleccionar tipo de lista ")
    print("2- Seleccionar algoritmo de orden ")
    print("2- REQ. 1: listar cronológicamente los artistas ")
    print("3- REQ. 2: listar cronológicamente las adquisiciones ")
    print("4- REQ. 3: clasificar las obras de un artista por técnica ") 
    print("5- REQ. 4: clasificar las obras por la nacionalidad de sus creadores ")
    print("6- REQ. 5: transportar obras de un departamento ")
    print("7- REQ. 6: proponer una nueva exposición en el museo ")
    print("0- Salir del programa ")

def initCatalog(tipo):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(tipo)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def pruebacomparacion(catalog):

    controller.ordenamiento(catalog) 

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:

        tipo = int(input("1- ARRAY_LIST\n2-LINKED_LIST\n "))
        if tipo == 1:
            tipo = 'ARRAY_LIST'
        elif tipo == 2:
            tipo = 'LINKED_LIST'
        else:
            break
        print("Cargando información de los archivos ....")
        catalog = initCatalog(tipo)
        loadData(catalog)
        print('Autores cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))

       
    elif int(inputs[0]) == 2:
        numelem = int(input("Digite el tamaño de la sub lista: "))

        A=(controller.tamano(catalog['artworks'], numelem))
        
    elif int(inputs[0]) == 3:
        pass
    elif int(inputs[0]) == 4:
        pass

    else:
        sys.exit(0)
sys.exit(0)
