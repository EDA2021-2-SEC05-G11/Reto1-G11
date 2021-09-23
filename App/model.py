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
from time import process_time 
import time 
import math
from time import process_time

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

    return Lista_final, ("Existen: "+str(lt.size(Lista_sort))+ " artistas según los años dados."), process_time()


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
    return resultado, process_time()

#Requerimiento 3

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
        print("Existen " + str(lt.size(obras_por_artista)) + " obras en el museo con su nombre\n")
        medium = buscar_medium(obras_por_artista)
        print("Existen " + str(len(medium)) + " diferentes tecnicas en sus obras de trabajo.\n")
        contador = contar_medios(medium)
        if len(contador)>=5:

            medios=lt.subList(contar_medios(medium), 1, 5)
        if len(contador)<1:
            return str('No hay obras')
        else:

            medios = contador
        print(medios)
        obras_tecnica = tecnica_mas_utilizada(medios, medium)
        resultado = eliminar_adicionales(obras_tecnica)

    return resultado, process_time()

def eliminar_adicionales(lista):

    resultado = []
    diccionario = {}
     
    for i in range(len(lista)):

     diccionario = {}
     diccionario["Title"] = lista[i]["Title"]
     diccionario["Date"]= lista[i]["Date"]
     diccionario["Medium"] = lista[i]["Medium"]
     diccionario["Dimensions"] = lista[i]["Dimensions"]

     resultado.append(diccionario)
    
    return resultado 


def tecnica_mas_utilizada(medios, lista_medios):

    mas_utilizado = lt.getElement(medios, 1)
    nombre= mas_utilizado["MediumName"]
    tecnicas = lista_medios[nombre]

    print("Su medio mas utilizado fue " + nombre)

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
#Requerimiento 4

def req4(catalog):
    
    Nacionalidades = lt.newList(datastructure='ARRAY_LIST')
    for i in range(1, lt.size(catalog['artworks'])+1):
        obras = lt.getElement(catalog['artworks'], i)
        id_autors = obras['ConstituentID']
        
        A = id_autors[1:len(id_autors)-1]
        A = A.split(', ')
        
        Lista_nueva = lt.newList()
        for id_a in A:
            lt.addLast(Lista_nueva, id_a)
        
        for id_art in range(1, lt.size(Lista_nueva)+1):
            Artista_id = lt.getElement(Lista_nueva, id_art)
            dicc = {}
            Pos = 1
            #print('entro al while')
            while Pos <= lt.size(catalog['artists']):
                Artista = lt.getElement(catalog['artists'], Pos)
                
                if Artista_id == Artista['ConstituentID']:
                    lt.insertElement(catalog['artworks'], Artista['DisplayName'], Pos)
                
                Pos += 1
                if len(Artista['Nationality']) > 1:
                    if Artista['Nationality'] in dicc:
                        dicc[Artista['Nationality']]+=1
                    else:
                        dicc[Artista['Nationality']]=1
    
    lt.addLast(Nacionalidades, dicc)
    dicc = sorted(dicc.items(), key=lambda x: x[1], reverse=True)
    print( dicc,  process_time())
    
#Requerimiento 5
def req5(Departamento, catalog):
    costo_segun_tam = 72.00
    costo_defecto = 48.00
    Costo_total_sin_info = 0
    Costo_total_con_info = 0
    Costo_total_translado = 0
    
    Lista_sin_info = lt.newList(datastructure='ARRAY_LIST')
    Lista_con_info = lt.newList(datastructure='ARRAY_LIST')
    Lista_obras_dept = lt.newList(datastructure='ARRAY_LIST')

    for i in range(1, lt.size(catalog['artworks'])+1):
        Obra = lt.getElement(catalog['artworks'], i)
        if Obra['Department'] == Departamento:
            lt.addLast(Lista_obras_dept, Obra)
        
            #Caso no obras con info suficiente

    for Obras in range(1, lt.size(Lista_obras_dept)+1):
        Obras_dept = lt.getElement(Lista_obras_dept, Obras)
        if Obras_dept['Dimensions'] == '' or Obras_dept['Dimensions'] == 'Variable' or Obras_dept['Dimensions'] == 'various' or Obras_dept['Dimensions'] == 'Various composition and sheet dimensions.' or Obras_dept['Dimensions'] == 'Various dimensions' or Obras_dept['Dimensions'] == 'Y':
            lt.addLast(Lista_sin_info,  Obras_dept)
            Costo_total_sin_info = (lt.size(Lista_sin_info)*costo_defecto)
    
            #Caso de obras con suficiente info

        elif Obras_dept['Dimensions'] != '' or Obras_dept['Dimensions'] != 'Variable' or Obras_dept['Dimensions'] != 'various' or Obras_dept['Dimensions'] != 'Various composition and sheet dimensions.' or Obras_dept['Dimensions'] != 'Various dimensions' or Obras_dept['Dimensions'] != 'Y':
                lt.addLast(Lista_con_info, Obras_dept)
   
    #Para circulos
    for Medidas in range(1, lt.size(Lista_con_info)+1):
        Medidas_obra = lt.getElement(Lista_con_info, Medidas)
        if  (Medidas_obra['Height (cm)'] != '' or Medidas_obra['Height (cm)'] !=0) and (Medidas_obra['Lenght (cm)'] != '' or Medidas_obra['Lenght (cm)'] !=0) and (Medidas_obra['Width (cm)'] != '' or Medidas_obra['Width (cm)'] !=0):
            A = float(Medidas_obra['Height (cm)']) * Medidas_obra['Lenght (cm)'] * Medidas_obra['Width (cm)']
            print(A)
    
    if Medidas_obra['Diameter (cm)']!=0 or Medidas_obra['Diameter (cm)']!='':
                cm_a_m = float(Medidas['Diameter (cm)'])/100
                Area_obra = math.pi*(cm_a_m/2)^2
                Costo_total_con_info = Area_obra*costo_segun_tam
                print(Costo_total_con_info)
    #Para figuras planas
    elif (Medidas_obra['Length (cm)']!= 0 or  Medidas_obra['Length (cm)']!='') and (Medidas_obra['Width (cm)']!= 0 or  Medidas_obra['Width (cm)']!=''):
            Area_cm_p = float(Medidas_obra['Length (cm)'])*float(Medidas_obra['Width (cm)'])
            Area_m = Area_cm_p/10000
            Costo_total_con_info = Costo_total_con_info+ (Area_m*costo_segun_tam)
            print(Costo_total_con_info)
    #Para figuras tridimensionales
    elif ((Medidas_obra['Length (cm)']!= 0 or  Medidas_obra['Length (cm)']!='') and (Medidas_obra['Width (cm)']!= 0 or  Medidas_obra['Width (cm)']!='') and (Medidas_obra['Height (cm)']!= 0 or  Medidas_obra['Height (cm)']!='')):
            Area_cm_t = float(Medidas_obra['Length (cm)'])*float(Medidas_obra['Width (cm)'])*float(Medidas_obra['Height (cm)'])
            Area_m = Area_cm_t/10000
            Costo_total_con_info = Costo_total_con_info + (Area_m*costo_segun_tam)
            print(Costo_total_con_info)
            print(Costo_total_con_info)
    return Costo_total_con_info, process_time()
         
#Requerimiento 6

def comparacionanio(a1, a2):
    return a1["Date"]<a2["Date"]

def req6(catalog, anio_inicial, anio_final, area_disponible):
    total_metros = 0

    lista = lt.newList(datastructure="ARRAY_LIST")
    for i in range(1, lt.size(catalog["artworks"])+1):
        obra = lt.getElement(catalog["artworks"], i)
        clasificacion = obra["Classification"] 
   
        if len(obra['Date']) != 0:

          if int(obra["Date"]) > anio_inicial and int(obra["Date"])< anio_final:

              if (clasificacion == "Drawing") or (clasificacion == "Painting") or (clasificacion == "Photograph") or (clasificacion == "Design") or (clasificacion == "Print"):

                 lt.addLast(lista, obra)
    
    lista_sort = sa.sort(lista, comparacionanio)
    lista_nombres= None

    for i in range(1, lt.size(lista_sort)+1):
        obra = lt.getElement(lista_sort, i)
        lista_nombres=id_a_lista(obra["ConstituentID"])
        lista_artistas= []
        for p in lista_nombres:
            for e in range(1, lt.size(catalog["artists"])+1):
                artistas = lt.getElement(catalog["artists"], e)

                if int(p) == int(artistas["ConstituentID"]):

                    lista_artistas.append(artistas["DisplayName"])
                    break 

        obra["ArtistsNames"] = lista_artistas

    lista_final = lt.newList(datastructure="ARRAY_LIST")

    for i in range(1, lt.size(lista_sort)+1):
        obra = lt.getElement(lista_sort, i)
        area= 0
        dic={}

        if len(obra["Height (cm)"]) > 0:

            if len(obra["Width (cm)"]) > 0:
                dic["Title"] = obra["Title"]
                dic["ArtistsNames"] = obra["ArtistsNames"]
                dic["Date"] = obra["Date"]
                dic["Classification"] = obra["Classification"]
                dic["Medium"] = obra["Medium"]
                dic["Dimensions"] = obra["Dimensions"]
                area= float(obra["Height (cm)"]) * float(obra["Width (cm)"])
                dic["Area"]= area * 0.0001
        
                lt.addLast(lista_final, dic)

    iterador = 0
    final = False
    ultimo_elemento = lt.size(lista_final)

    while iterador <= lt.size(lista_final) and final == False:

      elemento = lt.getElement(lista_final, iterador) 
      
      if float(total_metros) + elemento["Area"] < float(area_disponible):

       total_metros += elemento["Area"] 
       iterador += 1

      else:
          
       final = True
       ultimo_elemento = iterador -1

    print("Las obras a exponer serian " + str(ultimo_elemento))
    print("El area aproximada que se utiliza en m^2 es " + str(total_metros))

    lista_definitiva=lt.subList(lista_final, 1, ultimo_elemento)
    lista_a_retornar = None

    if lt.size(lista_definitiva) > 10:

       lista_a_retornar = lt.subList(lista_definitiva, 1, 3)
       lista_ultimos = lt.subList(lista_definitiva, lt.size(lista_definitiva)-3, 3)

       for i in range(1, lt.size(lista_ultimos)+1):
         lt.addLast(lista_a_retornar, lt.getElement(lista_ultimos, i))  

    else:

        lista_a_retornar = lista_definitiva


    return lista_a_retornar, process_time()
        

 
