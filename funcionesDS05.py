import json
import re
import os
from funcionesDS02 import *
from data_star import *

# >>>>>>>>>>>>>>>>>>>>PRIMERA PARTE<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 1.1
def imprimir_menu_desafio_5():
    imprimir_dato(""">>>>>>>>>>>>>>>>>>>>>>MENU PRINCIPAL<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    ---------------------------------------------------------------
A. LEER ARCHIVO
B. GUARDAR HEROE POR GENERO
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
G. Recorrer la lista y determinar la altura promedio de los superhéroes de
género M
H. Recorrer la lista y determinar la altura promedio de los superhéroes de
género F
I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (ítems C a F)
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
no tener, Inicializarlo con ‘No Tiene’).
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.
O. Listar todos los superhéroes agrupados por tipo de inteligencia
S- Salir""")

# 1.2
def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    opcion = input("Ingrese una de esas opciones: ")
    buscar = re.search("^[a-zA-Z]$", opcion)
    if buscar:
        return opcion.upper()
    else:
        return -1

# 1.3

def stark_marvel_app_5(lista: list) -> None:
    if not(lista and type(lista) == list):
        print("Error! Ingrese un a lista")
        return False
    while True:
        match(stark_calcular_imprimir_heroe()):
            case "A":
                lista = leer_archivo("data_star.json")
            case "B":
                pass
            case "C":
                pass 
            case "D":
                pass
            case "E":
                pass
            case "F":
                pass
            case "G":
                pass 
            case "H":
                pass
            case "I":
                pass
            case "J":
                pass
            case "K":
                pass 
            case "L":
                pass
            case "M":
                pass
            case "N":
                pass 
            case "O":
                pass
            case "S":
                break
            case -1:
                print("esa Opcion no existe")


# 1.4
def leer_archivo(archivo: str) -> list:
    if not(archivo and type(archivo) == str):  #Analiza si el el nombre del archivo no este vacio y que sea una cadena
        print("Formato no valido!")
        return
    with open(archivo, "r") as file:    #abro el archivo en modo lectura
        data = json.load(file)   #cargo los datos del archivo a una lista
    for valor in data.values():   #con esto obtengo el valor del heroe
        lista = valor  #lo asigno a otra variable
    return lista


# 1.5 

def guardar_archivo(archivo: str, contenido: str):
    with open(archivo, "w") as file:
        file.write(contenido)


# 1.6
def capitalizar_palabras(cadena: str) -> str:
    if type(cadena) != str:   #valido que sea tipo str
        return False
    palabras = cadena.split()  #divido la cadena por elementos a partir del espacio que los divide y lo devuelve en una lista
    for x in range(len(palabras)):
        palabras[x] = palabras[x].capitalize()  #capitalizo todas las palabra de la lista
    palabras_capitalizadas = " ".join(palabras)  #une cada palabra de lista divido por un espacio
    return palabras_capitalizadas  #lo retorna en una sola cadena

# 1.7

def obtener_nombre_capitalizado(diccionario: dict) -> str:
    nombre = diccionario["nombre"]  #obtiene el valor de la clave nombre
    nombre_capitalizado = capitalizar_palabras(nombre)   #paso el nombre ala funcion 
    return nombre_capitalizado   #retorno el nombre capitalizado


# 1.8
def obtener_nombre_y_dato(diccionario: dict, key: str) -> str:
    valor = diccionario[key]  #obtengo el valor
    nombre = obtener_nombre_capitalizado(diccionario)
    cadena = f"Nombre: {nombre} | {key}: {valor}"
    return cadena



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>SEGUNDA PARTE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 2.1
def es_genero(diccionario: dict, genero: str) -> bool:
    if genero == diccionario["genero"]:
        return True
    return False

# 2.2
def stark_guardar_heroe_genero(lista: list, genero: str):
    if genero != "M" and genero != "F": 
        print("Genero no valido!")
        return False
    datos = "NOMBRE,IDENTIDAD,EMPRESA,ALTURA,PESO,GENERO,COLOR_OJOS,COLOR_PELO,FUERZA,INTELIGENCIA" #definos las claves
    for heroe in lista:   #itero la lista
        if es_genero(heroe, genero):
            nombre = obtener_nombre_capitalizado(heroe)
            datos += f'\n{nombre},{heroe["identidad"]},{heroe["empresa"]},{float(heroe["altura"]):.2f},{float(heroe["peso"]):.2f},{heroe["genero"]},{heroe["color_ojos"]},{heroe["color_pelo"]},{heroe["fuerza"]},{heroe["inteligencia"]}'   #Concateno todos los valores en datos
    
    nombre_archivo = f"heroes_{genero}.csv"
    guardar_archivo(nombre_archivo, datos)
    return True

# -----------------------------------------

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TERCERA PARTE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
3.1
def calcular_min_genero(lista: list, key: str, genero: str) -> int or float:
    filtrado_genero = list(filter(lambda gen: gen["genero"] == genero.upper(), lista))  #Obtengo una lista con todos los personajes del genero ingresado
    flag = True
    for item in filtrado_genero:
        if(flag or item[key] < minimo):
            minimo = item[key]
            flag = False
    return minimo


# 3.2
def calcular_max_genero(lista: list, key: str, genero: str) -> int or float:
    filtrado_genero = list(filter(lambda gen: gen["genero"] == genero.upper(), lista)) #Obtengo una lista con todos los personajes del genero ingresado
    flag = True
    for item in filtrado_genero:
        if(flag or item[key] > maximo):
            maximo = item[key]
            flag = False
    return maximo

# 3.3
def calcular_max_min_dato_genero(lista: list, key: str, genero: str, flag_maximo: bool=True) -> (int or float):
    if flag_maximo:   #entra si la flag es true(esta por defecto)
        valor = calcular_max_genero(lista, key, genero)  #Obtengo el valor maximo
        heroe = list(filter(lambda heroe: heroe[key] == valor, lista))  #Me devuelve una lista de cada personaje con esa altura
    else:
        valor = calcular_min_genero(lista, key, genero) #Obtengo el valor minimo
        heroe = list(filter(lambda heroe: heroe[key] == valor, lista))
    return heroe

# 3.4
def stark_calcular_imprimir_guardar_heroe_genero(lista: list, key: str, genero: str, flag_maximo: bool=True) -> None:
    contenido = "NOMBRE,ALTURA"   #creo una variable con la cadena para las claves del csv
    if flag_maximo:
        calculo = "maximo"
        heroe = calcular_max_min_dato_genero(lista, key, genero)   #obtengo un diccionario del personaje o personajes con esa altura
        for dato in heroe:
            contenido += f"\n{dato['nombre']},{dato[key]}"  #concateno el resultado a contenido
            imprimir_dato(f"Mayor altura: {obtener_nombre_y_dato(dato, key)}")
    else:
        calculo = "minimo"
        heroe = calcular_max_min_dato_genero(lista, key, genero, flag_maximo)
        for dato in heroe:
            contenido += f"\n{dato['nombre']},{dato[key]}"
            imprimir_dato(f"Menor altura: {obtener_nombre_y_dato(dato, key)}")
    nombre_archivo = f"heroes_{calculo}_{key}_{genero}.csv"  #guardo una cadena con este formato con los argumentos recibido y sera el nombre del archivo.csv
    guardar_archivo(nombre_archivo, contenido)   #genero el archivo csv con el nombre_archivo y con el contenido




# stark_calcular_imprimir_guardar_heroe_genero(lista_heroe, "altura", "F")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>CUARTA PARTE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 4.1
def sumar_dato_heroe_genero(lista: list, key: str, genero: str) -> int or float:
    suma = 0
    for heroe in lista:
        if not(heroe and type(heroe) == dict):  #Si no es tipo diccionario o esta vacia, retorna False.
            return -1
        if(heroe["genero"] == genero.upper()):  #Entra al if si el genero del heroe coincide con el genero que se recibio por parametro.
            suma += heroe[key]
    return suma

# 4.2
def cantidad_heroes_genero(lista: list, genero: str) -> int:
    cantidad = 0
    for heroe in lista:
        if(heroe["genero"] == genero.upper()):
            cantidad += 1
    return cantidad

# 4.3
def calcular_promedio_genero(lista: list, key: str, genero: str) -> float:
    suma = sumar_dato_heroe_genero(lista, key, genero)
    cantidad = cantidad_heroes_genero(lista, genero)
    division = dividir(suma, cantidad)
    return round(division, 2)
# 4.4



def stark_calcular_imprimir_guardar_promedio_altura_genero(lista: list, key: str, genero: str) -> None:
    """recibe una lista, una clave tipo str y un genero valido("F" o "M"). Calcula el promedio de altura y muestra el resultado. El resultado lo guarda en un archivo.csv.
    """
    if not lista:
        return print("Error! La lista esta vacia")
    
    prom = calcular_promedio_genero(lista, key, genero)
    datos = f"Altura promeda genero {genero}: {prom}"
    nombre_archivo_csv = f"heroes_promedio_altura_{genero}.csv"
    imprimir_dato(datos)
    guardar_archivo(nombre_archivo_csv, datos)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>QUINTA PARTE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 5.1

def calcular_cantidad_tipo(lista: list, dato: str) -> dict:
    if not lista:   #si la lista vacia se ejecuta la siguiente linea de codigo.
        dic_error = {"ERROR": "La lista se encuentra vacía"}
        return print(dic_error)   #retorno el msj
    
    for item in lista:   #itero la lista
        item[dato] = capitalizar_palabras(item[dato])   #capitabilizo aquellas palabras que no lo estan

    lista_filtrada = set(map(lambda key: key[dato], lista))   #Devuelve una lista de valores sin repetir
    dicionario = {}
    for item in lista_filtrada:   #itero la lista filtrada
        con = 0
        for heroe in lista:   #itero la lista recibida dentro del bucle
            if(heroe[dato] == item):  #si el valor de la lista es igual al valor de item, entra a la siguiente linea de codigo
                con += 1   #cuento la cantidad de coincidencias
        dicionario[item] = con  #guardo en un diccionario como clave el valor de item y como valor la cantidad
    return dicionario

# 5.2

def guardar_cantidad_heroes_tipo(diccionario: dict, dato: str):
    archivo = ""
    for clave, valor in diccionario.items():
        archivo += f"Caracteristica: {clave} - Cantidad de heroes: {valor}\n"  #los concateno en una una sola variable
    nombre_archivo = f"heroes_cantidad_{dato}.csv"
    guardar_archivo(nombre_archivo, archivo)

# 5.3
def stark_calcular_cantidad_por_tipo(lista_original: list, dato: str):
    cantidad_por_tipo = calcular_cantidad_tipo(lista_original, dato)
    if type(cantidad_por_tipo) != dict:
        return False
    guardar_archivo(cantidad_por_tipo, dato)
    return True


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>SEXTA PARTE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 6.1
def obtener_lista_de_tipos(lista_heroe: list, datos: str):
    lista_valores = []
    for heroe in lista_heroe:
        valor = heroe[datos]    #guarda el valor del diccionario
        if valor == "":    #si no tiene valor su valor se remplaza por N/A
            valor = "N/A"
        lista_valores.append(valor)
    for x in range(len(lista_valores)):
        lista_valores[x] = capitalizar_palabras(lista_valores[x])   #capitabilizamos los valores
    lista_valores = set(lista_valores)  #quitamos repetidos
    return lista_valores

# 6.2
def normalizar_dato(dato: str, valor_default: str) -> str:
    if not dato:   #si esta vacia se ejecuta la siguiente linea de codigo
        dato = valor_default
    return dato
# 6.3
def normalizar_heroe(diccionario: dict, key: str):
    hereo_normalizado = {}
    nombre = capitalizar_palabras(diccionario["nombre"])
    valor = capitalizar_palabras(diccionario[key])
    valor = normalizar_dato(valor, "N/A")
    hereo_normalizado = {"nombre": nombre, key: valor}
    return hereo_normalizado

# 6.4
def obtener_heroes_por_tipo(heroes, tipos, tipo_dato):
    diccionario_variedades = {}

    for tipo in tipos:
        diccionario_variedades[tipo] = []

    for heroe in heroes:
        valor_tipo = heroe.get(tipo_dato, '')
        valor_tipo = valor_tipo.lower()

        for tipo in tipos:
            if tipo.lower() == valor_tipo:
                diccionario_variedades[tipo].append(heroe['nombre'])
                break

    return diccionario_variedades

# 6.5
def guardar_heroes_por_tipo(diccionario_variedades: dict, tipo_dato: str):
    mensaje = ""

    for tipo, nombres in diccionario_variedades.items():
        mensaje += f"{tipo} {tipo_dato.capitalize()}: "
        mensaje += ",".join(nombres)
        mensaje += "\n"

    archivo = f"heroes_segun_{tipo_dato}.csv"
    resultado = guardar_archivo(archivo, mensaje)

    return resultado
# 6.6
def stark_listar_heroes_por_dato(heroes, tipo_dato):
    tipos = obtener_lista_de_tipos(heroes, tipo_dato)
    diccionario_variedades = obtener_heroes_por_tipo(heroes, tipos, tipo_dato)
    resultado = guardar_heroes_por_tipo(diccionario_variedades, tipo_dato)
    return resultado
