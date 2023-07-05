import re
from data_star import lista_personajes
from FuncionesDS01 import *
from funcionesDS02 import *
import os

# 1.1. >>>>>>>>>>>>>>>>>>>>>>>>>
def extraer_iniciales(nombre_heroe: str) -> str:
    """Descripcion:
    obtiene las iniciales de una cadena a traves de un parametro.
    argumentos:
    parametro (str): Un string.
    retorna:
    str: Las iniciales de la cadena.
    N/A: Si la lista esta vacía."""
    if nombre_heroe:  #Si la cadena esta vacia o es un none retorna Falso, de lo contrario es True
        nombre_heroe = re.sub("-|the", " ", nombre_heroe)  #Si en la cadena encuentra un "the" o "-" lo remplaza por un espacio vacio
        obtener_inicial = re.findall(r"\b\w", nombre_heroe)  #Devuelve una lista con la primera letra de cada cadena
        iniciales = ".".join(obtener_inicial) + "."  #Une los elemento de la lista con un punto(.) y al final lo concatena con un punto(.)
        return iniciales  #Retorna las iniciales de la cadena
    else:
        return "N/A"  #esto retorna si la cadena esta vacia
    

# # 1.2. >>>>>>>>>>>>>>>>>>>>>>>
def definir_iniciales_nombre(heroe: dict, key: str) -> bool:
    """Agrega una nueva clave y valor al diccionario

    Args:
        heroe (dict): Un diccionario.
        key (str): Una clave string.

    Returns:
        True: Si el parametro heroe es un tipo diccionario(dic) y la clave (key) existe en el diccionario, devuelve el diccionario modificado.
        False: Si el valor heroe no es tipo dic o la clave(key) no se encuentre en el diccionario

    """
    if (type(heroe) != dict):  #si la condicion heroe recibida por parametro no es diccionario, entra al if y retorna un False
        print("Error! El heroe debe ser tipo dic")     
        return False
    if not(key in heroe.keys()):  #Verifica que la clave este en el diccionario recibido por heroe, sino esta, retorna False.
        print("la clave no se encuentra en el dic")
        return False
    iniciales = extraer_iniciales(heroe[key])  #Llamo a la funcion extraer_iniciales, le paso la clave del diccionario y obtengo las iniales de la clave y se lo designo a la variable
    heroe["iniciales"] = iniciales  #agrego una nueva clave y valor al diccionario heroe
    return True

# 1.3 >>>>>>>>>>>>>>>>>>
def agregar_iniciales_nombre(lista_heroe: list, key: str):
    """Recibe una lista de diccionario y lo recorre. Le agrega una nueva clave a la lista de diccionario.

    Args:
        lista_heroe (list): Una lista
        key (str): Una clave string

    Returns:
        True: Si es una lista y al menos tiene un elemento. devuelve la lista modificada con la nueva clave y valor
        False: Si no es una lista y la lista esta vacia.
    """
    if not (type(lista_heroe) == list):  #Si la condicion lista_heroe recibida por parametro no es una lista, entra al if y retorna False
        print("Error: lista_heroes debe ser del tipo lista")
        return False

    if len(lista_heroe) == 0:  #Si la lista recibida por parametro tiene cero elementos, entra al if y retorna un False
        print("Error: lista_heroes debe contener al menos un elemento")
        return False
    
    for heroe in lista_heroe: # la variable heroe recorre la lista lista_heroe recibida por parametro
        if not(definir_iniciales_nombre(heroe, key)):  #si la funcion no retorna un true, entra al if y retorna un false, devuelve la lista modificada
            print("Error, El origen de datos no contiene el formato correcto")
            return False
    return True

# 1.4. >>>>>>>>>>>>>>>>>>>>>>>>>>
def stark_imprimir_nombres_con_iniciales(lista_heroe: list, key: str) -> None:
    if not (type(lista_heroe) == list):  #Si la condicion lista_heroe recibida por parametro no es una lista, entra al if y retorna False
        print("Error: lista_heroes debe ser del tipo lista")
        return False

    if len(lista_heroe) == 0:  #Si la lista recibida por parametro tiene cero elementos, entra al if y retorna un False
        print("Error: lista_heroes debe contener al menos un elemento")
        return False
    if not(agregar_iniciales_nombre(lista_heroe, key)): #Si la funcion no retorna un true, entra al if y y retorna un false, de lo contrario devuelve la lista modificada
        return False
    for heroe in lista_heroe:  #la variable heroe recorre cada elemento de la lista(lista_heroe)
        print(f"* {heroe[key]} ({heroe['iniciales']})")  #Va mostrando por consola cada unos de los nombre e iniciales de los diccionarios de la lista(lista_heroe)

# stark_imprimir_nombres_con_iniciales(lista_personajes, "nombre")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# 2.1>>>>>>>>>>>>>>>>>>>

def generar_codigo_heroe(id_heroe: int, genero: str) -> str:
    """Recibe un id_hereo y un genero y genera una nueva clave de 10 digitos, si la clave no tiene 10 caracteres lo completa con 0 adelantes.
    Args:
        id_heroe (int): Tiene que ser un Id numero entero.
        genero (str): Tiene que recibir un genero que sea "F": femenino, M: "Masculino" y "NB": No binario. de lo contrario no sera valido.

    Returns:
        str: Retorna una clave de 10 digitos con el genero y el id_heroe, ej: X-0000000001. N/A sino es un genero valido.
    """
    if not((type(id_heroe) == int) and (genero == "M" or genero == "F" or genero == "NB")): #Si el id no es un numero entero y el genero no sea el indicado, retorna N/A
        return "N/A"
    tam = calcular_tam(str(id_heroe)) + calcular_tam(genero + "-")  #obtengo el tamaño del id_heroe mas genero y el guion
    acum = ""  # creo un acumulador con cadena vacias, para acumular str.
    for x in range(10 - tam):   #El maximo de caracteres es 10, asi que a 10 le resto al tam e itero esa cantidad de numero.
        acum += "0"   #le agrego al acumuludor un 0 en cada iteracion
    codigo_heroe = f"{genero}-{acum}{id_heroe}"  #concateno el genero, los ceros acumulados y el id y retorno el codigo.
    return codigo_heroe

# 2.2>>>>>>>>>>>>>>>>>>>>>>>>
def agregar_codigo_heroe(heroe: dict, id_heroe: int) -> bool:
    """Recibe un diccionario y le agrega una key y un value al diccionario

    Args:
        heroe (dict): tiene que ser tipo diccionario y no estar vacia para ser valida
        id_heroe (int): Tiene que ser un Id numero entero.
        genero (str): tiene que ser un genero valido.

    Returns:
        bool: True si esta todo valido. False si no es diccionario y el id no es un entero
    """
    #esta harcodeado pero asi decia la consigna
    if not heroe:  #Si el diccionario esta vacio es un booleano y devuelve false, entra al if y retorna false
        return False
    codigo_heroe = generar_codigo_heroe(id_heroe, heroe["genero"])   #paso los valores a la funcion generar_codigo_heroe
    if calcular_tam(codigo_heroe) != 10:  #si el codigo que devuelve no tiene 10 caracteres, entra al if y retorna false
        return False
    heroe["codigo_heroe"] = codigo_heroe   #agrego una clave "codigo_heroe" al diccionario y esa clave tiene el valor obtenido de codigo_heroe
    return True
# 2.3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def stark_generar_codigos_heroes(lista: list):
    """Reciba una lista de diccionarios. itera la lista, genera un id y obtiene el genero, genera un nuevo codigo con el id y el genero. Agrega una nueva clave y valor a los diccionarios.

    Args:
        lista (list): Tiene que ser tipo lista. NO estar vacia y tener de elementos diccionarios.
    Returns:
        bool: True Si esta todo valido. False si la lista esta vacia y no contiene diccionarios.
    """
    if not lista or calcular_tam(lista) == 0:   #si el diccionario esta vacio, Entra al if y retorna false
        print("El origen de datos no contiene el formato correcto")
        return False
    for heroe in lista:  #recorro la lista y obtengo los diccionarios
        if not (type(heroe) == dict) and "genero" not in heroe:  #si los elementos de la lista no son diccionario o no tiene la clave "genero" entra al if y retorna False
            print("El origen de datos no contiene el formato correcto")
            return False
    con = 0  #Creo un contador
    for heroe in lista:  #Recorro la lista y obtenie los diccionarios
        con += 1  #con el contador que con cada iteraion aumenta, obtengo la posicion de los elementos y genero el ID
        agregar_codigo_heroe(heroe, con)   #le paso el diccionario y el contador a la funcion y me devuelve un diccionario con la nueva clave y el codigo generado
    return True


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 3.1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def sanitizar_entero(numero_str: str) -> int:
    """Recibe un string de un numero entero y devuelve el numero transformado a entero.
    Args:
        numero_str (str): Un string con un numero entero.
    Returns:
        int: El numero transformado a entero. Si el numero ya es entero, lo devuelve igual.
        Retorna -1 si el numero no es entero.
        Retorna -2 si es un numero negativo.
    """
    if not type(numero_str) == str: #si el el valor recibido no es una cadena, lo devuleve igual. Esto para evitar un error.
        return numero_str
    numero_str = numero_str.strip()  #Si hay espacio al antes y despues del string, los quita.
    try:
        numero_entero = int(numero_str)   #transformo a entero la cadena.
        if numero_entero < 0:  #El numero entero es negativo. retorno -2
            return -2
    except ValueError:  #en el caso de no un entero, capturo el error y retorno -1
        return -1
    return numero_entero #Retorno el numero en entero.


# 3.2>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def sanitizar_flotante(numero_str: str) -> float:
    """Recibe un string de un numero flotante(con decimales) y devuelve el numero transformado a flotante.

    Args:
        numero_str (str): Un string con un numero flotante.

    Returns:
        float: El numero transformado a flotante. Si el numero ya es flotante, lo devuelve igual.
        Retorna -1 si el numero no es flotante.
        Retorna -2 si es un numero negativo.
    """
    if not type(numero_str) == str: #si el el valor recibido no es una cadena, lo devuleve igual. Esto para evitar un error.
        return numero_str
    numero_str = numero_str.strip()  #Si hay espacio al antes y despues del string, los quita.
    try:
        numero_flotante = float(numero_str)   #transformo a flotante la cadena.
        if numero_flotante < 0:  #El numero flotante es negativo. retorno -2
            return -2
    except ValueError:  #en el caso de no un flotante, capturo el error y retorno -1
        return -1
    return numero_flotante #Retorno el numero en flotante.

# 3.3>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def sanitizar_string(valor_str: str, valor_por_defecto: str="-") -> str:
    """Recibe un cadena y lo devuelve normalizado en miniscula.

    Args:
        valor_str (str): una cadena con caracteres no numericos.
        valor_por_defecto (str, optional): en el caso de que la cadena este vacia, puedes remplazarlo por un valor ingresado o por defecto lo remplaza con "-".

    Returns:
        str: una cadena normalizada en miniscula sin "/" y sin espacios en el principio y final.
    """
    valor_str = valor_str.strip()  #En el caso de haber espacios antes y despues de la cadena, los quita.
    valor_por_defecto = valor_por_defecto.strip()
    for char in valor_str:   #recorro la cadena y valido que cada caracter no sea un numero. En caso de serlo, retorna un "N/A"
        if char.isdigit():
            return "N/A"
    valor_str = re.sub("/", " ", valor_str)  #Si encuentra una barra "/", lo remplaza por espacio vacio.
    if valor_str:   #La cadena si tiene al menos un caracter, devuelve true y entra al if.
        return valor_str.lower()   #Retorna la cadena en minuscula.
    else:
        return valor_por_defecto.lower()  #en el caso de estar vacia, lo retorna en miniscula por el valor opcional o el valor por defecto.
    
# 3.4>>>>>>>>>>>>>>>>>>>>>>>>>>>>    
def sanitizar_dato(heroe: dict, clave: str, tipo_dato: str):
    """Recibe un diccionaio, una clave del diccionario y el tipo de dato que puede: "string", "entero" o "flotante".

    Args:
        heroe (dict): tiene que ser tipo diccionario para ser valido.
        clave (str): tiene que ser una clave valida del diccionario
        tipo_dato (str): "string": para normalizar una cadena de letras, "entero" para transformar a entero una cadena de numeros o "flotante": para transformar a numeros con decimales, una cadena de numeros flotantes.

    Returns:
        _type_: El string normalizado, el numero en entero o el numero flotante en flotante.
    """
    tipo_dato = tipo_dato.lower()  #convierto todo en minuscula el tipo de dato recibido

    if not(tipo_dato == "string" or tipo_dato == "entero" or tipo_dato == "flotante"):  #Si el tipo de dato recibido no es ninguno de esos 3, entra al if y retorna false
        print("Tipo de dato no reconocido")
        return False
    if clave not in heroe:  #si la clave recibida por parametro no se encuentra en el diccionario recibido. Entra al if y retorna false
        print('La clave especificada no existe en el héroe')
        return False
    if tipo_dato == "string":   #si tipo de dato es string, entra al if.
        heroe[clave] = sanitizar_string(heroe[clave])  #llamo a la funcion sanitizar_string y le paso el valor de la clave. Lo devuele normalizada.
    elif(tipo_dato == "entero"):   #si tipo de dato es entero, entra al if.
        heroe[clave] = sanitizar_entero(heroe[clave])   #llamo a la funcion sanitizar entero, le paso el valor de un numero entero en cadena y lo devuelve sin "".
    elif(tipo_dato == "flotante"):
        heroe[clave] = sanitizar_flotante(heroe[clave]) #llamo a la funcion sanitizar flotante, le paso el valor de un numero floante en cadena y lo devuelve sin "".
    return True


# 3.5>>>>>>>>>>>>>>>>>>>>>>>

def stark_normalizar_datos(lista_heroes):
    """Recibe una lista y normaliza la lista, altura los pasa a flotante, peso lo pasa a flotante, color de ojo lo pasa a minuscula e elimina la barra, color de pelo lo mismo que a color de ojo, fuerza lo transforma a entero e inteligencia lo normaliza y elimina las mayuscula o barras.

    Args:
        lista_heroes (_type_): Lista con al menos un elemento
    """
    if not lista_heroes:  #si la lista esta vacia, retorna false y entra al if
        print("Error: Lista de héroes vacía")
        return
    
    for heroe in lista_heroes:
        sanitizar_dato(heroe, 'altura', 'flotante')
        sanitizar_dato(heroe, 'peso', 'flotante')
        sanitizar_dato(heroe, 'color_ojos', 'string')
        sanitizar_dato(heroe, 'color_pelo', 'string')
        sanitizar_dato(heroe, 'fuerza', 'entero')
        sanitizar_dato(heroe, 'inteligencia', 'string')

    print("Datos normalizados")


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 4.1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def generar_indice_nombres(lista: list) -> list:
    """Recibe una lista de diccionarios, y devuelve una lista nueva con cada elemento que compone el nombre del personaje.

    Args:
        lista (list): debe ser una lista con al menos un elemento. La lista debe tener de elementos diccionarios, de lo contrario no sera valido.

    Returns:
        _type_: Una lista con los elementos de cada personaje
    """
    lista_nombre = []    #creo una lista vacia
    if not lista:   #Si la lista esta vacia, devuelve false y entra al if.
        print("El origen de datos no contiene el formato correcto")
        return
    for heroe in lista:  #Recorro la lista
        if not type(heroe) == dict:   #Si los elementos de la lista no son diccionarios, entra al if.
            print("El origen de datos no contiene el formato correcto")
            return
        if "nombre" not in heroe:   #si la clave nombre no se encuentra en el diccionario, entra al if.
            print("El origen de datos no contiene el formato correcto")
            return
        lista_nombre.extend(heroe["nombre"].split())   #Uso el metodo split para que me devuelva una lista con cada elemento de la lista del nombre.
        #uso el metodo extend para agregar los multiple elementos a la lista_nombre haciendo que sea una sola lista de elementos.
        # -------------------------------------------------------------
        #con expresiones regulares // otra manera
        # nombre = re.split(" ", heroe["nombre"])   #Divido los elementos por el espacio vacio y lo convierto en una lista.
        # for x in range(len(nombre)):  #recorro la lista creada
        #     lista_nombre.append(nombre[x])  #le agrego cada elemento de la lista nombre a lista_nombre
    
    return lista_nombre
# 4.2>>>>>>>>>>>>>>>>>>>>>>
def stark_imprimir_indice_nombre(lista_heroes: list):
    """Recibe una lista e impreme todos los elementos de los nombre unidos por un guion(-)

    Args:
        lista_heroes (list): Una lista
    """
    nombres = generar_indice_nombres(lista_heroes)   #Lllamo a la funcion, y le paso la lista. Me retorna una lista y se asigno a nombres
    nombres_juntos = "-".join(nombres)  #uno los elementos de la lista con un guion "-"
    print(nombres_juntos)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 5.1>>>>>>>>>>>>>>>>>>>>>>>
def convertir_cm_a_mtrs(valor_cm: float) -> float:
    if type(valor_cm) != float:
        return -1
    valor_mt = valor_cm / 100
    return valor_mt
# 5.2>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def generar_separador(patron: str, largo: int, imprimir: bool=True):
    """Recibe un patron y lo muliplica por el largo. El tercer parametro en un bool, por default esta en true y genera un separador.

    Args:
        patron (str): Un caracter como minino y dos como maximo
        largo (int): Un numero entero entre 1 y 235
        imprimir (bool, optional): True: Para imprimir el separador, False: para retornar el separador. sino recibe un tercer parametro. Por default esta en True.
    """
    if not(1 <= len(patron) <= 2) or not(1 <= largo <= 235):  #Si el patron es menor a 1 y mayor a 2 o el largo es menor a 1 y mayor a 235, entra al if y retorna "N/A"
        return "N/A"
    separador = patron * largo  #multiplico el caracter por el largo y lo guardo en separador
    if not imprimir:  #si el valor booleano no es true. Retorna el separador, de lo contrario, lo imprime.
        return separador
    print(separador)
# 5.3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def generar_encabezado(titulo):
    generar_separador("*", 100)
    print(titulo)
    generar_separador("*", 100)

# 5.4>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def imprimir_ficha_heroe(heroe: dict):
    heroe["altura"] = convertir_cm_a_mtrs(heroe["altura"])
    generar_encabezado("PRINCIPAL")
    print(f"""
    NOMBRE DEL HÉROE:               {heroe['nombre']}               
    IDENTIDAD SECRETA:              {heroe['identidad']} 
    CONSULTORA: Marvel Comics       {heroe['empresa']}
    CÓDIGO DE HÉROE : M-00000001    {heroe['codigo_heroe']}
    """)
    generar_encabezado("FISICO")
    print(f"""
    ALTURA:                         {heroe['altura']:.2f} Mtrs.               
    PESO:                           {heroe['peso']} Kg.
    FUERZA:                         {heroe['fuerza']} 
    """)
    generar_encabezado("SEÑAS PARTICULARES")
    print(f"""
    COLOR DE OJOS:                  {heroe['color_ojos']}               
    COLOR DE PELO:                  {heroe['color_pelo']} 
    """)

# 5.5>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def stark_navegar_fichas(lista_heroes: list):
    contador = 0
    tam = len(lista_heroes)
    while True:
        os.system("cls")
        print("""
        [ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir
        """)
        opcion = input("Ingrese una opción: ")
        os.system("cls")
        if opcion == "1":
            contador = (contador - 1) % tam  #Le resto uno al contador y consigo el resto del contador, devolvera siempre el mismo numero mientra no sea igual al tamaño de la lista
            imprimir_ficha_heroe(lista_heroes[contador])
        elif opcion == "2":
            contador = (contador + 1) % tam
            imprimir_ficha_heroe(lista_heroes[contador])
        elif opcion == "s":
            break
        else:
            print("opcion incorrecta")
        os.system("pause")

# /////////////////////////////////////////////////////////////////////////////////////

# 6.1
def imprimir_menu():
    print("""
    1 - Imprimir la lista de nombres junto con sus iniciales
    2 - Generar códigos de héroes
    3 - Normalizar datos
    4 - Imprimir índice de nombres
    5 - Navegar fichas
    S - Salir
    ____________________________________________________________
    """)

def stark_menu_principal():
    imprimir_menu()
    opcion = input("Ingrese una opcion: ")
    return opcion

def stark_marvel_app_3(lista_heroe: list):
    flag = False
    while True:
        os.system("cls")
        opcion = stark_menu_principal()
        os.system("cls")
        match(opcion):
            case "1":
                stark_imprimir_nombres_con_iniciales(lista_heroe, "nombre")
            case "2":
                stark_generar_codigos_heroes(lista_heroe)
                flag = True
            case "3":
                stark_normalizar_datos(lista_heroe)
            case "4":
                stark_imprimir_indice_nombre(lista_heroe)
            case "5":
                if flag:
                    stark_navegar_fichas(lista_heroe)
                else:
                    print("primero debes generar el codigo heroe")
            case "s":
                break
            case _:
                print("opcion no valida")
        os.system("pause")

