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


from DISClib.DataStructures.arraylist import addLast
import config as cf
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
def DateComparisonLower(date1, date2):
    #Determina si Date1 es menor a Date2
    State = True
    if len(date1) > 0 and len(date2) > 0:
        year_date1 = int(date1[0:3])
        year_date2 = int(date2[0:3])
        month_date1 = int(date1[5:6])
        month_date2= int(date2[5:6])
        day_date1 = int(date1[8:])
        day_date2 = int(date2[8:])
        if year_date1 > year_date2:
            State = False
        if year_date1 == year_date2:
            if month_date1 > month_date2:
                State = False
            if month_date1 == month_date2:
                if day_date1 > day_date2:
                    State = False
    else:
        State = False
    return State

def DateComparisonHigher(date1, date2):
    #Determina si Date1 es mayor a Date2
    State = True
    if len(date1) > 0 and len(date2) > 0:
        year_date1 = int(date1[0:3])
        year_date2 = int(date2[0:3])
        month_date1 = int(date1[5:6])
        month_date2= int(date2[5:6])
        day_date1 = int(date1[8:])
        day_date2 = int(date2[8:])
        if year_date1 < year_date2:
            State = False
        if year_date1 == year_date2:
            if month_date1 < month_date2:
                State = False
            if month_date1 == month_date2:
                if day_date1 < day_date2:
                    State = False
    else:
        State = False
    return State

def ArtistName(catalog, id):
    artists = catalog['artist']
    NamesList = []

    return NamesList
# Funciones de consulta
def ArtworkAcquired(catalog, date1, date2):
    obras = catalog['artworks']
    acquired_cont = 0
    purchase_cont = 0
    Nuevalista = lt.newList()
    for i in range(lt.size(obras)-lt.size(obras), lt.size(obras)-1):
        templist = lt.getElement(catalog['artworks'], i)
        if DateComparisonHigher(templist['DateAcquired'], date1) == True and DateComparisonLower(templist['DateAcquired'], date2) == True:
            acquired_cont += 1
            lt.addLast(Nuevalista, [templist['Title'], ArtistName(catalog, templist['ConstituentID']), templist['Date'], templist['Medium'], templist['Dimensions']])
            if templist['CreditLine'][:8] == 'Purchase' or templist['CreditLine'][:8] == 'purchase':
                purchase_cont += 1
    resp_1 = 'El número de obras adquiridas en ese rango es: ' + str(acquired_cont)
    resp_2 = 'El número de obras compradas en ese rango es: ' + str(purchase_cont)
    AnswerList = lt.newList()
    lt.addLast(AnswerList, ['Title', 'ArtistName', 'Date', 'Medium', 'Dimensions'])
    return (resp_1, resp_2, Nuevalista)

def cmpfunctionDateAcquired(date1, date2):
    State = True
    year_date1 = int(date1[0:3])
    year_date2 = int(date2[0:3])
    month_date1 = int(date1[5:6])
    month_date2= int(date2[5:6])
    day_date1 = int(date1[8:])
    day_date2 = int(date2[8:])
    if year_date1 > year_date2:
        State = False
    if year_date1 == year_date2:
        if month_date1 > month_date2:
            State = False
        if month_date1 == month_date2:
            if day_date1 > day_date2:
                State = False
    return State 
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
