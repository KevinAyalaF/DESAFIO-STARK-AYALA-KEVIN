from data_star import lista_personajes

def transformar_a_entero_o_flotante(valor: str) -> int or float:
    """Recibe un string de numero y dependiendo del tipo de numero, retorna un entero o flotante.
    Si la cadena no es numerico, retorna la misma cadena."""
    flag = False
    try:
        valor = int(valor)
        flag = True
    except ValueError:
        try:
            valor = float(valor)
            flag = True
        except ValueError:
            pass
    return flag, valor
    
def stark_normalizar_datos(lista: list) -> list:
    """Recibe una lista de diccionarios y recorre cada elemento de la lista. 
    Luego recorre cada clave y valor del diccionario, convirtiendolo a entero o flotante dependiendo del tipo de numero.
    En el caso de no haber un valor numerico, directamente pasa y va por la siguiente clave.
    Esto retorna la misma lista con todos los valores numericos transformado a entero o flotante
    """
    if lista:
        flag_datos = False
        for diccionario in lista:
            try:
                for clave, valor in diccionario.items():
                    flag_convertido, numero = transformar_a_entero_o_flotante(valor)
                    if flag_convertido:
                        diccionario[clave] = numero
                        flag_datos = True
            except AttributeError:
                break
        if flag_datos:
                print("datos normalizados")
    else:
        print("la lista esta vacia")

    return lista


#1.1
def obtener_nombre(dicionario: dict) -> str:
    """Recibe un diccionario y retorna el nombre"""
    nombre = f'Nombre: {dicionario["nombre"]}'
    return nombre

# 1.2
def imprimir_dato(cadena: str) -> None:
    """Recibe una cadena y lo imprime"""
    print(cadena)
# 1.3
def stark_imprimir_nombres_heroes(lista: list) -> None:
    """Recibe una lista e imprime todos los nombres"""
    if lista:
        for heroe in lista:
            imprimir_dato(obtener_nombre(heroe))
    else:
        return -1
    
# 2.0
def obtener_nombre_y_dato(diccionario: dict, key: str):
    """Recibe un diccionario y retorna El nombre y un dato"""
    datos = f"Nombre: {diccionario['nombre']} | {key}: {diccionario[key]}"
    return datos
# 3.0
def stark_imprimir_nombres_alturas(lista: list, key: str) -> None:
    if lista:
        for heroe in lista:
            imprimir_dato(obtener_nombre_y_dato(heroe, key))
    else:
        return -1


# 4.1
def calcular_max(lista: list, key: str) -> int or float:
    """Recibe una lista y una clave. Recorre la lista y obtiene el valor maximo y lo retorna"""
    flag = True
    for heroe in lista:
        if flag:
            max = heroe[key]
            flag = False
        elif(heroe[key] > max):
            max = heroe[key]
    return max

# 4.2
def calcular_min(lista: list, key: str) -> int or float:
    """Recibe una lista y una clave. Recorre la lista y obtiene el valor minimo y lo retorna"""
    flag = True
    for heroe in lista:
        if flag:
            min = heroe[key]
            flag = False
        elif(heroe[key] < min):
            min = heroe[key]
    return min

# 4.3
def calcular_max_min_dato(lista: list, valor: str, key: str) -> int or float:
    """Recibe una lista, el tipo de valor y una clave. Si el tipo de valor es 'maximo' retorna el numero maximo,
    si el tipo de valor es 'minimo' retorna el numero minimo"""
    if valor == "maximo":
        num = calcular_max(lista, key)
    elif(valor == "minimo"):
        num = calcular_min(lista, key)
    return num
# 4.4    
def stark_calcular_imprimir_heroe(lista: list, valor: str, key: str) -> None:
    """Recibe una lista, el tipo de valor y una clave. Si el tipo de valor es 'maximo' retorna el numero maximo y el nombre relacionado al numero,
    si el tipo de valor es 'minimo' retorna el numero minimo y el nombre relacionado al numero"""
    if lista:
        num = calcular_max_min_dato(lista, valor, key)
        for heroe in lista:
            if heroe[key] == num:
                imprimir_dato(obtener_nombre_y_dato(heroe, key))
    else:
        return -1
    
# 5.1
def sumar_dato_heroe(lista: list, key: str) -> int or float:
    """Recibe una lista y una clave. Recorre la lista y suma todos los valores de la clave.
    Retorna la suma"""
    suma = 0
    for heroe in lista:
        if heroe:
            suma += float(heroe[key])
    return suma
# 5.2
def dividir(dividendo: int or float, divisor: int or float) -> float:
    """Recibe 2 numeros. Si el divisor es 0, retorna 0.
    Retorna el resultado de la division"""
    if divisor != 0:
        division = dividendo / divisor
    else:
        return 0
    return division
# --
def calcular_tam(secuencia):
    contador = 0
    for elemento in secuencia:
        contador += 1
    return contador

# 5.3
def calcular_promedio(lista: list, key: str) -> float:
    """Recibe una lista y una clave. Calcula la cantidad de numeros y la suma total de eso numeros, Los divide
    y retorna el promedio"""
    tam = calcular_tam(lista)
    sum = sumar_dato_heroe(lista, key)
    division = sum / tam
    return division
# 5.4
def stark_calcular_imprimir_promedio_altura(lista: list, key: str, msj = str) -> None:
    """Recibe una lista, una clave y un mensaje. Escribe el mensaje que quieres imprimir y lo retornara con el promedio"""
    if lista:
        prom = calcular_promedio(lista, key)
        imprimir_dato(f"{msj} {prom:.2f}Cm")
    else:
        return -1

# 6.1
def impimir_menu():
    imprimir_dato(""">>>>>>>>>>>>>>>>>>>>>>MENU PRINCIPAL<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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
    10-salir""")

# 6.2 
def validar_entero(cadena: str) -> bool:
    try:
        entero = int(cadena)
        return True
    except ValueError:
        return False
# 6.3
def stark_menu_principal():
    impimir_menu()
    numero = input("ingrese un numero: ")
    if validar_entero(numero):
        return int(numero)
    else:
        return -1
    
# 7.1
import os
def stark_marvel_app_2(lista: list):
    while True:
        os.system("cls")
        opcion = stark_menu_principal()
        match(opcion):
            case 1:
                stark_imprimir_nombres_heroes(lista)
            case 2:
                stark_imprimir_nombres_alturas(lista, "altura")
            case 3:
                print("La altura maxima es:", calcular_max_min_dato(lista, "maximo", "altura"),"Cm")
            case 4:
                print("La altura minima es:", calcular_max_min_dato(lista, "minimo", "altura"),"Cm")
            case 5:
                stark_calcular_imprimir_promedio_altura(lista, "altura", "El promedio de altura es:")
            case 6:
                stark_calcular_imprimir_heroe(lista, "maximo", "altura")
            case 7:
                stark_calcular_imprimir_heroe(lista, "minimo", "altura")
            case 8:
                stark_calcular_imprimir_heroe(lista, "maximo", "peso")
            case 9:
                stark_calcular_imprimir_heroe(lista, "minimo", "peso")
            case 10:
                salida = input("estas seguro que quieres salir? s/n: ")
                if salida == "s":
                    break
            case _:
                print("opcion incorrecta")
        os.system("pause")

# def generar_codigo_heroe(id_heroe, genero_heroe):
#     id_str = str(id_heroe).zfill(10)  # Convierte el id_heroe a string y completa con ceros a la izquierda hasta tener 10 caracteres
#     codigo_heroe = f"{genero_heroe}-{id_str}"
#     return codigo_heroe


# stark_marvel_app(lista_personajes)