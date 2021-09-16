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
import datetime as dt
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import quicksort as qs
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'artist': None,
               'artworks': None,}

    catalog['artist'] = lt.newList()
    catalog['artworks'] = lt.newList()

    return catalog

# Funciones para agregar informacion al catalogo

def addArtWork(catalog, artwork):
    lt.addLast(catalog['artworks'],artwork)

def addArtist(catalog, artist):
    lt.addLast(catalog['artist'],artist)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def sortcatalog(catalogo,tipo_ordenamiento):
    if tipo_ordenamiento == "1":
         catalogo_ordenado = ins.sort(catalogo)
    elif tipo_ordenamiento == "2":
        catalogo_ordenado = mer.sort(catalogo)
    elif tipo_ordenamiento == "3":
        catalogo_ordenado = sa.sort(catalogo)
    elif tipo_ordenamiento == "4":
        catalogo_ordenado = qs.sort(catalogo)
    else:
        catalogo_ordenado = catalogo
    return catalogo_ordenado
    
def cmpArtworkByDateAcquired(artwork1, artwork2):
    day=artwork1[12][0]+artwork1[12][1]
# Funciones de ordenamiento
