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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2. Tamaño de la muestra")
    print("3- requerimiento 1")
    print("4- requerimiento 2")
    print("5- requerimiento 3")
    print("6- requerimiento 4")
    print("7- requerimiento 5")
    print("8- requerimiento 6")

catalog = None

def initCatalog():

    return controller.initCatalog()

def newCatalog2():
    catalog = {'artist': None,
               'artworks': None,}

    catalog['artist'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['artworks'] = lt.newList(datastructure='ARRAY_LIST')

    return catalog

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def sublist(catalogo,muestra):
    """
    Crea una Sublista con un tamaño de muestra dado
    """
    if muestra <= lt.size(catalogo):
        sublista = lt.subList(catalogo,0,muestra)
    else:
        sublista = "El tamaño de la muestra es mayor al tamaño del catalogo"
    return sublista



"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        input2= input("Seleccione 1 para SINGLE_LINKED o 2 para ARRAY_LIST\n")
        if int(input2) == 1:
            print("Cargando información de los archivos ....")
            catalog = initCatalog()
            loadData(catalog)
            print('obras de arte cargadas: ' + str(lt.size(catalog['artworks'])))
            print('artistas cargado: ' + str(lt.size(catalog['artist'])))
            print('los tres ultimos artistas son:')
            artistas = catalog['artist']
            for cont in range(lt.size(catalog['artist'])-2, lt.size(catalog['artist'])+1):
                artista = lt.getElement(artistas, cont)
                print(artista['DisplayName'])
            print('las tres ultimas obras son:')
            obras = catalog['artworks'] 
            for cont in range(lt.size(catalog['artworks'])-2, lt.size(catalog['artworks'])+1):
                obra = lt.getElement(obras, cont)
                print(obra['Title'])
        elif int(input2) == 2:
            print("Cargando información de los archivos ....")
            catalog = newCatalog2()
            loadData(catalog)
            print('obras de arte cargadas: ' + str(lt.size(catalog['artworks'])))
            print('artistas cargado: ' + str(lt.size(catalog['artist'])))
            print('los tres ultimos artistas son:')
            artistas = catalog['artist']
            for cont in range(lt.size(catalog['artist'])-2, lt.size(catalog['artist'])+1):
                artista = lt.getElement(artistas, cont)
                print(artista['DisplayName'])
            print('las tres ultimas obras son:')
            obras = catalog['artworks'] 
            for cont in range(lt.size(catalog['artworks'])-2, lt.size(catalog['artworks'])+1):
                obra = lt.getElement(obras, cont)
                print(obra['Title'])


    elif int(inputs[0]) == 2:
        muestra = int(input("Escriba el tamaño de la muestra: "))
        catalog = initCatalog()
        loadData(catalog)
        sublista = sublist(catalog["artworks"], muestra)
        print(sublista)

    elif int(inputs[0]) == 3:
        print("Escoja el tipo de ordenamiento..")
        print("1. Insertion")
        print("2. Sheel")
        print("3. Merge")
        print("4. Quick")
        tipo_ordenamiento = input("Escriba el numero de la opción: ")
        catalog = initCatalog
        loadData(catalog)
        

    else:
        sys.exit(0)
sys.exit(0)
