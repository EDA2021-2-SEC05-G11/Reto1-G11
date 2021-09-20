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


from DISClib.DataStructures.arraylist import iterator, newList
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as me
assert cf
from datetime import datetime
import time 

# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

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
    p2 = None

    if len(e1) > 0 :
        e1 = datetime.strptime(e1, '%Y-%m-%d') 
        p1 = True
    else:
        p1 = False

        
    if len(e2) > 0:
        e2 = datetime.strptime(e2, '%Y-%m-%d') 
        p2= True
    else:
        p2 = False

    if p1==False:
        return (False)
    if p2==False:
        return (False)
    if p1==True and p2==True:
    
     if e1 < e2:
        
        return (True)

     else:

        return(False)     

def menu():
    print("opciones") 
    print("1- Shellsort")
    print("2- Insertionsort")
    print("3- quicksort")
    print("4- mergesort")

def crearsublista(lst, numelem):
    n=True
    while n==True:
        menu()
        algo = int(input("elegir algoritmo "))
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

def comparacionfechas(a1, a2):
    return a1['BeginDate']<a2['BeginDate']

def id_a_lista(string):

    un_digito=True

    if "," in string:
      un_digito=False

    valores = string[1:len(string)-1]  

    if un_digito == False:

        resultado = valores.split(",")

    else:

        resultado = [valores]

    return resultado 



#Requerimiento 1
def req1(catalog, año_ini, año_fini):
    Lista = lt.newList(datastructure='ARRAY_LIST')
    for i in range(1, lt.size(catalog['artists'])+1):
        artista = lt.getElement(catalog['artists'], i)
        if artista['BeginDate'] != '' or artista['BeginDate']!=0:
            if int(artista['BeginDate'])> año_ini and int(artista['BeginDate'])<año_fini:
                lt.addLast(Lista, artista)
    
    Lista_sort = sa.sort(Lista, comparacionfechas)
    Lista_final = lt.subList(Lista_sort, 1, 3)
    Lista_ultimos = lt.subList(Lista_sort, lt.size(Lista_sort)-3, 3)
    for i in range(1, lt.size(Lista_ultimos)+1):
        lt.addLast(Lista_final, lt.getElement(Lista_ultimos, i))

    return Lista_final, ("Existen: "+str(lt.size(Lista_sort))+ " artistas según los años dados.")


#Requerimiento 2 

def purchase(lista):

    cantidad = 0

    for i in range(1, lt.size(lista)+1):

      obra=lt.getElement(lista, i)

      if obra["CreditLine"].lower() ==  "purchase":

          cantidad += 1

    return (cantidad)  

def resultado_final_con_id(lista, catalog):
    
    resultado=lt.newList(datastructure='ARRAY_LIST')  
    artists = catalog["artists"]
    iterador = 0
    diccionario={}
    artistas= ""

    for i in range(1, lt.size(lista)+1):

        diccionario={}
        obra = lt.getElement(lista,i)
        lista_obra = id_a_lista(obra["ConstituentID"])
        artistas= ""

        for n in lista_obra:
       
          iterador = 0  
          encontrado = False 
          
          while iterador <= lt.size(artists) and encontrado != True:

           artista = lt.getElement(artists,iterador)

           if int(n) == int(artista["ConstituentID"]):

            artistas += artista["DisplayName"]
            encontrado = True 

           else: 

            iterador += 1 
     
        diccionario["ObjectID"] = obra["ObjectID"]
        diccionario["Title"] = obra["Title"]
        diccionario["ArtistsName"] = artistas
        diccionario ["Medium"] = obra["Medium"]
        diccionario["Dimensions"] = obra["Dimensions"]
        diccionario["Date"] = obra["Date"] 
        diccionario["DateAcquired"] = obra["DateAcquired"]
        diccionario["URL"] = obra["URL"]

        lt.addLast(resultado, diccionario)    
      
    return resultado          

def req2(catalog,fecha_inicial, fecha_final):

    artworks = catalog["artworks"]

    lista = lt.newList(datastructure='ARRAY_LIST')

    for i in range(1, lt.size(artworks)+1):

        obra = lt.getElement(artworks, i)

        if len(obra['DateAcquired']) > 0:

            lt.addLast(lista, obra)

    fecha_inicial=datetime.strptime(fecha_inicial, '%Y-%m-%d') 
    fecha_final= datetime.strptime(fecha_final, '%Y-%m-%d') 
    rango = lt.newList(datastructure='ARRAY_LIST')   

    for i in range(1, lt.size(lista)+1):

        comp = lt.getElement(lista, i)
        fecha=datetime.strptime(comp['DateAcquired'], '%Y-%m-%d') 

        if fecha >= fecha_inicial and fecha <= fecha_final:

            lt.addLast(rango, comp)

    if lt.size(rango)< 1:

      return("No se encontraron obras dentro del rango dado" )

    lista_sort = sa.sort(rango, comparacionDateAcquired)  
    lista_final = lt.subList(lista_sort, 1, 3)
    lista_ultimos = lt.subList(lista_sort, lt.size(lista_sort)-3, 3)

    for i in range(1, lt.size(lista_ultimos)+1):
        lt.addLast(lista_final, lt.getElement(lista_ultimos, i))  

    compra=purchase(lista_sort)         

    print ("Existen: " + str(lt.size(lista_sort)) + " obras en el rango de los años dados.")
    print ("Existen " + str(compra) + " obras adquiridas por compra")

    resultado=resultado_final_con_id(lista_final, catalog)
    return resultado

#Requerimiento 3

def obtener_id(artistas, nombre):
    id = None 

    for i in range(1, lt.size(artistas)+1):

        artista=lt.getElement(artistas, i)
        if nombre in artista["DisplayName"].lower() or nombre == artista["DisplayName"]:

           id= int(artista["ConstituentID"])
           break 
        
        else:

            pass

    return id
def req3(catalog, nombre):

    obras= catalog["artworks"]
    artistas= catalog["artists"]
    id = obtener_id(artistas, nombre.lower())
    obras_por_artista = lt.newList(datastructure="ARRAY_LIST")
    contar_obras = 0
    resultado = None

    if id == None:

       resultado="El artista no fue encontrado dentro de nuestro catalogo"

    else: 

        for i in range(1, lt.size(obras)+1):

          obra = lt.getElement(obras, i)
          lista = id_a_lista(obra["ConstituentID"])

          for s in lista: 

           if id == int(s):

            lt.addLast(obras_por_artista, obra)
            contar_obras += 1
            break

        medium = buscar_medium(obras_por_artista)
        print("Existen " + str(len(obras_por_artista)) + " obras en el museo con su nombre")
        print("Existen " + str(len(medium)) + " diferentes tecnicas en sus obras de trabajo.")
        medios=lt.subList(contar_medios(medium), 1, 5)
        print(medios)
        resultado = tecnica_mas_utilizada(medios, medium)

    return resultado 

def tecnica_mas_utilizada(medios, lista_medios):

    mas_utilizado = lt.getElement(medios, 1)
    nombre= mas_utilizado["MediumName"]
    tecnicas = lista_medios[nombre]

    return tecnicas

def comparar_mayor(e1,e2):

    return e1["Count"] > e2["Count"]



def contar_medios(medios):

    lista = lt.newList(datastructure="ARRAY_LIST")

    for i in medios:
        
        dic = {}
        dic["MediumName"] = i
        dic["Count"] = len(medios[i])
        lt.addLast(lista, dic)

    sa.sort(lista, comparar_mayor)

    return lista

def buscar_medium(lista):

    diccionario={}

    for i in range(1, lt.size(lista)+1):

       obra = lt.getElement(lista, i)    

       if obra["Medium"] in diccionario:

           diccionario[obra["Medium"]].append(obra)

       else:

           diccionario[obra["Medium"]]=[obra]

    return diccionario 







