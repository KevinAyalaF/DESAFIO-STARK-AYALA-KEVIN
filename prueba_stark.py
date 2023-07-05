from data_star import *



# def mostrar_heroe_fila(heroe: dict) -> None:
#     print(f"{heroe['nombre']} {heroe['identidad']}")



# for heroe in lista_personajes:
#     mostrar_heroe_fila(heroe)
    


# def filtrar_heroe(lista: list, key: str, color: str) -> list:
#     lista_filtrada = []
#     for heroe in lista:
#         if heroe[key] == color:
#             lista_filtrada.append(heroe)

#     return lista_filtrada


# l = filtrar_heroe(lista_personajes, "genero", "F")

# print(l)



# def filtrar(lista, key):
#     lista_filtrada = []
#     for item in lista:
#         if not item[key] in lista_filtrada:
#             lista_filtrada.append(item[key])
    
#     return lista_filtrada



# lista = filtrar(lista_personajes, "color_ojos")
# print(lista)

# def esta_en_lista(lista: list, item: str) -> bool:
#     esta = False
#     for elemento in lista:
#         if elemento == item:
#             esta = True
#             break
#     return esta


# def quitar_repetidos(lista: list) -> list:
#     lista_sin_repe = []
#     for item in lista:
#         if(not esta_en_lista(lista_sin_repe, item)):
#             lista_sin_repe.append(item)
    
#     return lista_sin_repe

# Crear una lista vacía para contener los diccionarios
# lista_de_diccionarios = []

# # Crear un bucle para permitir que el usuario agregue diccionarios hasta que decida detenerse
# while True:
#     # Crear un diccionario vacío para que el usuario lo llene
#     nuevo_diccionario = {}

#     # Permitir que el usuario agregue claves y valores al diccionario
#     while True:
#         clave = input("Ingrese una clave para el diccionario (o presione enter para terminar): ")
#         if not clave:
#             break
#         valor = input(f"Ingrese el valor para la clave '{clave}': ")
#         nuevo_diccionario[clave] = valor

#     # Agregar el diccionario lleno a la lista
#     lista_de_diccionarios.append(nuevo_diccionario)

#     # Preguntar al usuario si desea agregar otro diccionario
#     continuar = input("¿Desea agregar otro diccionario? (s/n): ")
#     if continuar.lower() != "s":
#         break

# # Imprimir la lista completa de diccionarios
# print(lista_de_diccionarios)


# def proyectar_heroes(lista: list, valor: str, valor_2: str = None) -> list:
#     lista_nueva = []
#     for item in lista:
#         if not valor_2 == None:
#             lista_nueva.append([item[valor], item[valor_2]])
#         else:
#             lista_nueva.append(item[valor])
#     return lista_nueva

# def mostrar_heroes(lista: list, titulo: str) -> None:
#     if len(lista[0]) == 2:
#         print(titulo)
#         print("----------------")
#         for item in lista:
#             print(f'{item[0]:20s} {item[1]}')
#     else:
#         print(titulo)
#         print("------------------------------")
#         for item in lista:
#             print(item)

# l = proyectar_heroes(lista_personajes, "nombre", "peso")
# mostrar_heroes(l, "nombres")



# for inicial in iniciales:
#     if(inicial != "t"):
#         pass

# nombre = "Howard the Duck"
# name = re.sub("the", "", nombre)
# names = re.findall(r"\b\w", name)
# iniciales = ".".join(names) + "."
# print(iniciales)

