#python3 estendertela.py

import os
from time import sleep


def xrandr():
    print("[1] DIREITA")
    print("[2] ESQUERDA")
    


def direita():
    os.system("xrandr --auto --output VGA-1 --right-of DVI-I-1")
    os.system("clear")
    print("se não estendeu como você queria digite outro numero")
    xrandr()
    tela2()


def esquerda():
    os.system("xrandr --auto --output DVI-I-1 --right-of VGA-1")
    os.system("clear")
    print("se não estendeu como você queria digite outro numero")
    xrandr()
    tela2()


def tela2():
    tela = int(input("digite um numero para estender a tela para direita ou esquerda:"))
    if tela == 1:
        direita()
    if tela == 2:
        esquerda()


    

# inicio da execução do código

xrandr()


tela = int(input("digite um numero para estender a tela para direita ou esquerda:"))


if tela == 1:
    direita()


if tela == 2:
    esquerda()
