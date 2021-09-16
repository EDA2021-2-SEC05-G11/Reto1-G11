"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as me
assert cf
from datetime import datetime
import time 


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def newCatalog(tipo):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None,
               }

    catalog['artists'] = lt.newList(datastructure=tipo)
    catalog['artworks'] = lt.newList(datastructure=tipo)

    return catalog



# Funciones para agregar informacion al catalogo

def addartists(catalog, artists):
    # Se adiciona el artista a la lista de artistas
    lt.addLast(catalog['artists'], artists)  

def addartworks(catalog, artworks):
    # Se adiciona el artista a la lista de artistas
    lt.addLast(catalog['artworks'], artworks)
    
   

def comparacionDateAcquired(e1, e2): 
    e1 = e1['DateAcquired']
    e2 = e2['DateAcquired']
    p1 = None
    P2 = None

    if len(e1) != 0 or None or '':
        e1 = datetime.strptime(e1, '%Y-%m-%d') 
        p1 = True
    else:
        p1 = False

        
    if len(e2) != 0 or None or '':
        e2 = datetime.strptime(e2, '%Y-%m-%d') 
        p2= True
    else:
        p2 = False

    if p1==False:
        return (False)
    if p2==False:
        return (True)
    if p1==True and p2==True:
    
     if e1 < e2:
        
        return (True)

     else:

        return(False)     

def menu():
    print("opciones") 
    print("1- Shellsort")
    print("2-Insertionsort")
    print("3- quicksort")
    print("4- mergesort")

def crearsublista(lst, numelem):
    n=True
    while n==True:
        menu()
        algo = int(input("elegir algorit "))
        if algo == 1:
          algo =sa
          n=False
        elif algo == 2:
           algo = ins
           n=False
        elif algo == 3:
             algo = qs 
             n=False
        elif algo == 4:
            algo = me 
            n=False
        else:
            print("elija una opcion valida")
        

    sub_list = lt.subList(lst, 1, numelem)
    sorted_list = algo.sort(sub_list, comparacionDateAcquired)
    
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = algo.sort(sub_list, comparacionDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print(elapsed_time_mseg)
    return elapsed_time_mseg, sorted_list

#Req 1
def comparacionbegindate(a1, a2):
    return a1['BeginDate']<a2['BeginDate']
def req1(catalog, año_ini, año_fini):
    Lista = lt.newList(datastructure='ARRAY_LIST')
    for i in range(1, lt.size(catalog['artists'])+1):
        artista = lt.getElement(catalog['artists'], i)
        if artista['BeginDate'] != '' or artista['BeginDate']!=0:
            if int(artista['BeginDate'])> año_ini and int(artista['BeginDate'])<año_fini:
                lt.addLast(Lista, artista)
    
    Lista_sort = sa.sort(Lista, comparacionbegindate)
    Lista_final = lt.subList(Lista_sort, 1, 3)
    Lista_ultimos = lt.subList(Lista_sort, lt.size(Lista_sort)-3, 3)
    for i in range(1, lt.size(Lista_ultimos)+1):
        lt.addLast(Lista_final, lt.getElement(Lista_ultimos, i))

    return Lista_final












