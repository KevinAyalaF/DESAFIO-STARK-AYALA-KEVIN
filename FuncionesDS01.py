from data_star import *
import os

def mostrar_menu():
    print(""">>>>>>>>>>>>>>>>>>>>>>MENU PRINCIPAL<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    ---------------------------------------------------------------
    1-Mostrar Nombre de todos los superheroes
    2-Mostrar el nombre y altura de todos los superheroes
    3-Mostrar mayor altura
    4-Mostrar menor altura
    5-Mostrar promedio de la altura
    6-Mostrar el nombre de la altura mayor
    7-Mostrar el nombre de la altura menor
    8-Mostrar el mayor peso
    9-Mostrar el menor peso
    10-Mas opciones
    11-salir""")
    opcion = input("Ingrese una opcion: ")
    return opcion

def mostrar_segundo_menu():
    print(""">>>>>>>>>>>>>>>>>>>>>>>>MENU<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    1-Mostrar Nombres de superheroes masculinos
    2-Mostrar Nombres de superheroes femeninos
    3-Mostrar Superheroe masculino mas alto
    4-Mostrar Superheroe femenino mas alto
    5-Mostrar Superheroe masculino mas bajo
    6-Mostrar Superheroe femenino mas bajo
    7-Mostrar promedio de altura de supeheroes masculinos
    8-Mostrar promedio de altura de supeheroes femeninos
    9-Mostrar nombre Superheroe masculino mas alto
    10-Mostrar Nombre Superheroe masculino mas bajo
    11-Mostrar Nombre Superheroe femenino mas alto
    12-Mostrar Nombre Superheroe femenino mas bajo
    13-Mostrar cantidad de colores de ojos de los heroes
    14-Mostrar cantidad de colores de pelos de los heroes
    15-Mostrar cantidad de tipo de inteligencia de los heroes
    16-Mostrar nombre de los heroe por su color de ojos
    17-Mostrar nombre de los heroe por su color de pelo
    18-Mostrar nombre de heroe por su inteligencia
    19-Volver al inicio
    20-Salir""")
    opcion = input("Ingrese una opcion: ")
    return opcion


def copiar_lista(lista_origen: list, lista: list) -> list:
    for clave in lista_origen:
        lista.append(clave.copy())
    return lista

def stark_normalizar_datos(lista_diccionarios):
    for diccionario in lista_diccionarios:
        for clave, valor in diccionario.items():
            try:
                diccionario[clave] = int(valor)
            except ValueError:
                try:
                    diccionario[clave] = float(valor)
                except ValueError:
                    pass
    return lista_diccionarios


def filtrar_lista(lista: list, key: str, valor: str) -> list:
    lista_filtrada = []
    for value in lista:
        if value[key] == valor:
            lista_filtrada.append(value)
    
    return lista_filtrada


def proyectar_heroe(lista: list, valor: str) -> list:
    lista_nueva = []
    for item in lista:
        lista_nueva.append(item[valor])
    return lista_nueva

def mostrar_heroe(lista: list, titulo: str) -> None:
    print(titulo)
    print("------------------------------")
    for item in lista:
        print(item)

# --------------------------------------------------------------------------------------------
def proyectar_heroes(lista: list, valor: str, valor_2: str = None) -> list:
    lista_nueva = []
    for item in lista:
        dic = {}
        if not valor_2 == None:
            dic[valor] = item[valor]
            dic[valor_2] = item[valor_2]
            lista_nueva.append(dic)
        else:
            lista_nueva.append(item[valor])
    return lista_nueva

def mostrar_heroes(lista: list, titulo: str, valor: str = None, valor_2: str = None) -> None:
    if not(valor == None and valor_2 == None):
        print(titulo)
        print("----------------")
        for item in lista:
            print(f'{item[valor]:20s} {item[valor_2]}')
    else:
        print(titulo)
        print("------------------------------")
        for item in lista:
            print(item)
# -------------------------------------------------------------------------------------------------------


def flotabilizar_lista(lista: list, valor: str, valor_2: str = None) -> list:
    lista_nueva = []
    for item in lista:
        if valor_2 == None:
            item[valor] = float(item[valor])
        else:
            item[valor] = float(item[valor])
            item[valor_2] = float(item[valor_2])
    for item in lista:
        lista_nueva.append(item)
    return lista_nueva



def calcular_mayor_o_menor(lista: list, key: str, tipo: bool=True) -> list:
    valor = lista[0][key]
    if tipo:
        for item in lista:
            if ((item[key] > valor) or item[key] < valor):
                valor = item[key]
    return valor

def repetidos(lista: list, valor: float, key: str, key_2: str) -> list:
    lista_nueva = []
    for item in lista:
        if item[key] == valor:
            lista_nueva.append(item[key_2])
    return lista_nueva

def calcular_promedio(lista: list, key: str) -> None:
    acum = 0
    for item in lista:
        acum += item[key]
    prom = acum / len(lista)
    return prom

def esta_en_lista(lista: list, item: str) -> bool:
    esta = False
    for elemento in lista:
        if elemento == item:
            esta = True
            break
    return esta


def quitar_repetidos(lista: list) -> list:
    lista_sin_repe = []
    for item in lista:
        if(not esta_en_lista(lista_sin_repe, item)):
            lista_sin_repe.append(item)
    return lista_sin_repe



def mostrar_tipos(lista_filtrada: list, lista: list, mensaje: str, key_1: str, key_2: str) -> None:
    for item in lista_filtrada:
        print(mensaje + item)
        for valor in lista:
            if valor[key_1] == item:
                print(valor[key_2])
        print("-------------------------------")



def mostrar_cantidad(lista_filtrada: list, lista: list, mensaje: str, key: str) -> None:    
    for item in lista_filtrada:
        contador = 0
        for valor in lista:
            if (valor[key] == item):
                contador += 1
        print(f'{mensaje} {item} son: {contador}')


def contar(x: str, valor: str) -> int:
    contador = 0
    for item in x:
        if(item == valor):
            contador += 1
    return contador




# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





def star_marvel_app_1(lista_original):
    lista_copiada = []
    copiar_lista(lista_original, lista_copiada)
    lista_copiada = stark_normalizar_datos(lista_copiada)
    while True:
        os.system("cls")
        match(mostrar_menu()):
            case "1":
                nombre = proyectar_heroe(lista_copiada, "nombre")
                mostrar_heroe(nombre, "Todos los nombres de los superheroes es:")
            case "2":
                heroe = proyectar_heroes(lista_copiada, "nombre", "altura")
                mostrar_lista = mostrar_heroes(heroe, "nombre              Altura", "nombre", "altura")
            case "3":
                altura = calcular_mayor_o_menor(lista_copiada, "altura")
                print(f"la mayor altura es: {altura}cm")
            case "4":
                altura = calcular_mayor_o_menor(lista_copiada, "altura", False)
                print(f"la menor altura es: {altura}cm")
            case "5":
                print(f'el promedio de altura es: {calcular_promedio(lista_copiada, "altura"):.2f}cm')
            case "6":
                heroe = proyectar_heroe(filtrar_lista(lista_copiada, "altura", calcular_mayor_o_menor(lista_copiada, "altura")), "nombre")
                mostrar_heroe(heroe, "los nombres de los superheroe con la mayor altura es")
            case "7":
                heroe = proyectar_heroe(filtrar_lista(lista_copiada, "altura", calcular_mayor_o_menor(lista_copiada, "altura", False)), "nombre")
                mostrar_heroe(heroe, "los nombres de los superheroe con la menor altura es")
            case "8":
                heroe = proyectar_heroe(filtrar_lista(lista_copiada, "peso", calcular_mayor_o_menor(lista_copiada, "peso")), "nombre")
                mostrar_heroe(heroe, "los nombres de los superheroe con el mayor peso es")
            case "9":
                heroe = proyectar_heroe(filtrar_lista(lista_copiada, "peso", calcular_mayor_o_menor(lista_copiada, "peso", False)), "nombre")
                mostrar_heroe(heroe, "los nombres de los superheroe con el menor peso es: ")
            case "10":
                while True:
                    heroes_femeninos = filtrar_lista(lista_copiada, "genero", "F")
                    heroes_masculinos = filtrar_lista(lista_copiada, "genero", "M")
                    flag_salida = False
                    os.system("cls")
                    match(mostrar_segundo_menu()):
                        case "1":
                            mostrar_heroe(proyectar_heroe(filtrar_lista(lista_copiada, "genero", "M"), "nombre"), "los nombres de los superheroes masculinos son: ")
                        case "2":
                            mostrar_heroe(proyectar_heroe(filtrar_lista(lista_copiada, "genero", "F"), "nombre"), "los nombres de los superheroes femeninos son: ")
                        case "3":
                            print("la mayor altura del genero masculino es: ", calcular_mayor_o_menor(heroes_masculinos, "altura"), "cm")
                        case "4":
                            print("la mayor altura deel genero femenino es: ", calcular_mayor_o_menor(heroes_femeninos, "altura"), "cm")
                        case "5":
                            print("la menor altura del genero masculino es: ", calcular_mayor_o_menor(heroes_masculinos, "altura", False), "cm")
                        case "6":
                            print("la menor altura del genero femenino es: ", calcular_mayor_o_menor(heroes_femeninos, "altura", False), "cm")
                        case "7":
                            print(f"el promedio de altura de los heroes masculino es: {calcular_promedio(heroes_masculinos, 'altura'):.2f}")
                        case "8":
                            print(f"el promedio de altura de los heroes femeninos es: {calcular_promedio(heroes_femeninos, 'altura'):.2f}")
                        case "9":
                            mayor_altura_masculino = proyectar_heroe(filtrar_lista(heroes_masculinos, "altura", calcular_mayor_o_menor(heroes_masculinos, "altura")), "nombre")
                            mostrar_heroe(mayor_altura_masculino, "Superheroe masculino con mayor altura son:")
                        case "10":
                            mayor_altura_femenino = proyectar_heroe(filtrar_lista(heroes_femeninos, "altura", calcular_mayor_o_menor(heroes_femeninos, "altura")), "nombre")
                            mostrar_heroe(mayor_altura_femenino, "Superheroe femenino con mayor altura son:")
                        case "11":
                            mayor_altura_masculino = proyectar_heroe(filtrar_lista(heroes_masculinos, "altura", calcular_mayor_o_menor(heroes_masculinos, "altura", False)), "nombre")
                            mostrar_heroe(mayor_altura_masculino, "Superheroe masculino con menor altura son:")
                        case "12":
                            mayor_altura_femenino = proyectar_heroe(filtrar_lista(heroes_femeninos, "altura", calcular_mayor_o_menor(heroes_femeninos, "altura", False)), "nombre")
                            mostrar_heroe(mayor_altura_femenino, "Superheroe femenino con menor altura son:")
                        case "13":
                            sin_repetidos = quitar_repetidos(proyectar_heroe(lista_copiada, "color_ojos"))
                            mostrar_cantidad(sin_repetidos, lista_copiada, "la cantidad de heroe con el ojos color", "color_ojos")
                        case "14":
                            sin_repetidos = quitar_repetidos(proyectar_heroe(lista_copiada, "color_pelo"))
                            mostrar_cantidad(sin_repetidos, lista_copiada, "la cantidad de heroe con el pelo color", "color_pelo")
                        case "15":
                            sin_repetidos = quitar_repetidos(proyectar_heroe(lista_copiada, "inteligencia"))
                            mostrar_cantidad(sin_repetidos, lista_copiada, "la cantidad de heroe con inteligencia", "inteligencia")
                        case "16":
                            sin_repetidos = quitar_repetidos(proyectar_heroe(lista_copiada, "color_ojos"))
                            mostrar_tipos(sin_repetidos, lista_copiada, "color: ", "color_ojos", "nombre")
                        case "17":
                            sin_repetidos = quitar_repetidos(proyectar_heroe(lista_copiada, "color_pelo"))
                            mostrar_tipos(sin_repetidos, lista_copiada, "color: ", "color_pelo", "nombre")
                        case "18":
                            sin_repetidos = quitar_repetidos(proyectar_heroe(lista_copiada, "inteligencia"))
                            mostrar_tipos(sin_repetidos, lista_copiada, "inteligencia: ", "inteligencia", "nombre")
                        case "19":
                            break
                        case "20":
                            flag_salida = True
                            break
                        case _:
                            print("esa opcion no existe")
                    os.system("pause")
                if flag_salida:
                    break
            case "11":
                break
            case _:
                print("esa opcion no existe")
        os.system("pause")

