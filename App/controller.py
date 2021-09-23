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


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtWorks(catalog)
    loadArtists(catalog)

def loadArtWorks(catalog): 
    artfile = cf.data_dir + 'Artworks-utf8-small.csv' 
    input_file = csv.DictReader(open(artfile, encoding='utf-8'))  
    for artWork in input_file:
        model.addArtWork(catalog, artWork)

def loadArtists(catalog): 
    artfile = cf.data_dir + 'Artists-small-utf8.csv' 
    input_file = csv.DictReader(open(artfile, encoding='utf-8'))  
    for artist in input_file:
        model.addArtist(catalog, artist)  

def ordenamiento_cronologico(catalogo_principal, fecha_inicial, fecha_final):
    lista_ordenada = model.ordenar_cronologicamente(catalogo_principal,fecha_inicial,fecha_final)
    return lista_ordenada

def clasificacion_tecnica(catalogo_principal, nombre):
    lista_obras = model.clasificacion_tecnica(catalogo_principal,nombre)
    return lista_obras
