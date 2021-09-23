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
 """

import config as cf
import model
import csv
from datetime import datetime


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo
def initCatalog(tipo):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(tipo)
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadartists(catalog)
    loadartworks(catalog)

def loadartists(catalog):
    """
    Carga los artistas del archivo.  Por cada obra se toman sus artistas y por
    cada uno de ellos, se crea en la lista de artistas, a dicho artista y una
    referencia a la obra que se esta procesando.
    """
    artistsfile = cf.data_dir + '/MoMA/Artists-utf8-large.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artists in input_file:
        artists["BeginDate"]= int(artists["BeginDate"])
        
        model.addartists(catalog, artists)

def loadartworks(catalog):
    artworksfile = cf.data_dir + '/MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artworks in input_file:
        model.addartworks(catalog, artworks)

def tamano(lst, numelem):
    
    return model.crearsublista(lst, numelem)

#Requerimientos
def req1(catalog, año_ini, año_fini):
    return model.req1(catalog, año_ini, año_fini)

def req2(catalog, fecha_inicial, fecha_final):
    return model.req2(catalog, fecha_inicial, fecha_final)

def req3(catalog, nombre):
    return model.req3(catalog, nombre)

def req4(catalog):
    return model.req4(catalog)
def req5(Departamento, catalog):
    return model.req5(Departamento, catalog)

def req6(catalog, anio_inicial, anio_final, area_disponible):
    return model.req6(catalog, anio_inicial, anio_final, area_disponible)