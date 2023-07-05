from FuncionesDS01 import star_marvel_app_1
from funcionesDS02 import stark_marvel_app_2
from funcionesDS03 import stark_marvel_app_3
from funcionesDS05 import *
import os


def menu_stark():
    print("""-----------MENU DESAFIOS STARK-----------
    1-DESAFIO STARK 01
    2-DESAFIO STARK 02
    3-DESAFIO STARK 03
    4-DESAFIO STARK 05
    5-SALIR""")

def menu_principal():
    menu_stark()
    opcion = input("ingrese una opcion: ")
    return opcion


def stark_marvel_desafios_app():
    while True:
        os.system("cls")
        opcion = menu_principal()
        match(opcion):
            case "1":
                star_marvel_app_1(lista_personajes)
            case "2":
                stark_marvel_app_2(lista_personajes)
            case "3":
                stark_marvel_app_3(lista_personajes)
            case "4":
                pass
            case "5":
                break
        os.system("pause")
