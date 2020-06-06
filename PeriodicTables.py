import webbrowser
import os
import math
import time
from help import help
from info import info
from tqdm import tqdm
from copyrights import copyright
from update import update
from question import question
from PIL import Image
from manual import manual
from PeriodicTable import H
from PeriodicTable import He
from PeriodicTable import Li
from PeriodicTable import Be
from PeriodicTable import B
from PeriodicTable import C
from PeriodicTable import N
from PeriodicTable import O
from PeriodicTable import F
from PeriodicTable import Ne
from PeriodicTable import Na
from PeriodicTable import Mg
from PeriodicTable import Al
from PeriodicTable import Si
from PeriodicTable import P
from PeriodicTable import S
from PeriodicTable import Cl
from PeriodicTable import Ar
from PeriodicTable import K
from PeriodicTable import Ca
from PeriodicTable import Sc
from PeriodicTable import Ti
from PeriodicTable import V
from PeriodicTable import Cr
from PeriodicTable import Mn
from PeriodicTable import Fe
from PeriodicTable import Co
from PeriodicTable import Ni
from PeriodicTable import Cu
from PeriodicTable import Zn
from PeriodicTable import Ga
from PeriodicTable import Ge
from PeriodicTable import As
from PeriodicTable import Se
from PeriodicTable import Br
from PeriodicTable import Kr
from PeriodicTable import Rb
from PeriodicTable import Sr
from PeriodicTable import Y
from PeriodicTable import Zr
from PeriodicTable import Nb
from PeriodicTable import Mo
from PeriodicTable import Tc
from PeriodicTable import Ru
from PeriodicTable import Rh
from PeriodicTable import Pd
from PeriodicTable import Ag
from PeriodicTable import Cd
from PeriodicTable import In
from PeriodicTable import Sn
clear = lambda: os.system("cls")
start = "start"
load = "Loading..."
print(load)
time.sleep(3)
l1 = "Configuring Periodic Table..."
print(l1)
time.sleep(2)
for x in tqdm(range(100)):
    time.sleep(0.1)
clear()
time.sleep(1)
print("Welcome To Periodic Tables Version 1.4.7!!!")
time.sleep(1)
print("The new Version of Periodic Table is released!")
time.sleep(1)
print("If you are new in this program, enter \"help\", \"info\", \"copyright\" for more informations")
time.sleep(1)
print("you can checked the updated contents. type \"updated\"")
time.sleep(1)
print("※!!!!!BEFORE USING THIS PROGRAM PLEASE TYPE \"manual\"!!!!!※")
time.sleep(1)
print("More function and elements will be Updated.")
time.sleep(1)
print("This program is made by JWare Soft Development Team")
time.sleep(1)
print("Copyright ⓒ JWare Soft Develoment Team 2019")
time.sleep(1)
print("*Do Not Change This Program. With any Permissions.*")
time.sleep(1)
print("Do not use the source code of this program for commercial purposes.")
time.sleep(0.5)
print("IF YOU WANT TO START, TYPE \"start\"!")
while math.inf:
    Start = input(">>>")
    if(Start == start):
        clear()
        print("Wait.....")
        time.sleep(1)
        clear()
        print("==============================================================================================")
        print("Periodic Table Ver 1.4.7-------Made By JWare Soft Development Team")
        print("Copyright ⓒ JWare Soft Develoment Team 2019")
        print("If you are new in this program, enter \"help\", \"info\", \"copyright\" for more informations")
        print("you can checked the updated contents. type \"updated\"")
        print("※!!!!!BEFORE USING THIS PROGRAM PLEASE TYPE \"manual\"!!!!!※")
        print("If you want to quit this program, type quit and Press Enter")
        print("==============================================================================================")
        break;
count = 1
while math.inf:
    cse = input(">>>")
    if(cse == "help"):
        help()
    if (cse == "info"):
        info()
    if (cse == "copyright"):
        copyright()
    if(cse == "H" or cse == "h" or cse == "1"):
        H()
    if(cse == "He" or cse == "he" or cse == "2"):
        He()
    if(cse == "Li" or cse == "li" or cse == "3"):
        Li()
    if(cse == "Be" or cse == "be"):
        Be()
    if(cse == "B" or cse == "b"):
        B()
    if(cse == "C" or cse == "c"):
        C()
    if(cse == "N" or cse == "n"):
        N()
    if (cse == "O" or cse == "o"):
        O()
    if (cse == "F" or cse == "f"):
        F()
    if (cse == "Ne" or cse == "ne"):
        Ne()
    if (cse == "Na" or cse == "na"):
        Na()
    if (cse == "Mg" or cse == "mg"):
        Mg()
    if (cse == "Al" or cse == "al"):
        Al()
    if (cse == "Si" or cse == "si"):
        Si()
    if (cse == "P" or cse == "p"):
        P()
    if (cse == "S" or cse == "s"):
        S()
    if (cse == "Cl" or cse == "cl"):
        Cl()
    if (cse == "Ar" or cse == "ar"):
        Ar()
    if (cse == "K" or cse == "k"):
        K()
    if (cse == "Ca" or cse == "ca"):
        Ca()
    if (cse == "Sc" or cse == "sc"):
        Sc()
    if (cse == "Ti" or cse == "ti"):
        Ti()
    if (cse == "V" or cse == "v"):
        V()
    if (cse == "Cr" or cse == "cr"):
        Cr()
    if (cse == "Mn" or cse == "mn"):
        Mn()
    if (cse == "Fe" or cse == "fe"):
        Fe()
    if (cse == "Co" or cse == "co"):
        Co()
    if (cse == "Ni" or cse == "ni"):
        Ni()
    if (cse == "Cu" or cse == "cu"):
        Cu()
    if (cse == "Zn" or cse == "zn"):
        Zn()
    if (cse == "Ga" or cse == "ga"):
        Ga()
    if (cse == "Ge" or cse == "ge"):
        Ge()
    if (cse == "As" or cse == "as"):
        As()
    if (cse == "Se" or cse == "se"):
        Se()
    if (cse == "Br" or cse == "br"):
        Br()
    if (cse == "Kr" or cse == "kr"):
        Kr()
    if (cse == "Rb" or cse == "rb"):
        Rb()
    if (cse == "Sr" or cse == "sr"):
        Sr()
    if (cse == "Y" or cse == "y"):
        Y()
    if (cse == "Zr" or cse == "zr"):
        Zr()
    if (cse == "Nb" or cse == "nb"):
        Nb()
    if (cse == "Mo" or cse == "mo"):
        Mo()
    if (cse == "Tc" or cse == "tc"):
        Tc()
    if (cse == "Ru" or cse == "ru"):
        Ru()
    if (cse == "Rh" or cse == "rh"):
        Rh()
    if (cse == "Pd" or cse == "pd"):
        Pd()
    if (cse == "Ag" or cse == "ag"):
        Ag()
    if (cse == "Cd" or cse == "cd"):
        Cd()
    if (cse == "In" or cse == "in"):
        In()
    if (cse == "Sn" or cse == "sn"):
        Sn()
    if (cse == "0704"):
        time.sleep(1)
        print("You found an EasterEgg!!!")
        time.sleep(1)
        print("Congratulation!")
        time.sleep(1)
        print("There are nothing...")
        time.sleep(1)
        print("but...")
        time.sleep(1)
        print("I will applaud you!")
    if (cse == "quit"):
        print("                        ")
        print("Shut down the processor.")
        print("Periodic-Tables JWare Soft Development 1.3b.4 Version")
        print("Press the Enter.")
        break
    if (cse == "clear"):
        clear()
        print("==============================================================================================")
        print("Periodic Table Ver 1.4.7-------Made By JWare Soft Development Team")
        print("Copyright ⓒ JWare Soft Develoment Team 2019")
        print("If you are new in this program, enter \"help\", \"info\", \"copyright\" for more informations")
        print("you can checked the updated contents. type \"updated\"")
        print("※!!!!!BEFORE USING THIS PROGRAM PLEASE TYPE \"manual\"!!!!!※")
        print("If you want to quit this program, type quit and Press Enter")
        print("==============================================================================================")

    if (cse == "updated"):
        update()
    if (cse == "reload"):
        clear()
        reload = "Reloading..."
        print(reload)
        time.sleep(3)
        l1 = "Configuring Periodic Table..."
        print(l1)
        time.sleep(2)
        for x in tqdm(range(100)):
            time.sleep(0.1)
        clear()
        time.sleep(1)
        print("Welcome To Periodic Tables Version 1.4.7!!!")
        time.sleep(1)
        print("The new Version of Periodic Table is released!")
        time.sleep(1)
        print("If you are new in this program, enter \"help\", \"info\", \"copyright\" for more informations")
        time.sleep(1)
        print("you can checked the updated contents. type \"updated\"")
        time.sleep(1)
        print("※!!!!!BEFORE USING THIS PROGRAM PLEASE TYPE \"manual\"!!!!!※")
        time.sleep(1)
        print("More function and elements will be Updated.")
        time.sleep(1)
        print("This program is made by JWare Soft Development Team")
        time.sleep(1)
        print("Copyright ⓒ JWare Soft Develoment Team 2019")
        time.sleep(1)
        print("*Do Not Change This Program. With any Permissions.*")
        time.sleep(1)
        print("Do not use the source code of this program for commercial purposes.")
        time.sleep(0.5)
        print("IF YOU WANT TO START, TYPE \"start\"!")
        while math.inf:
            Start = input(">>>")
            if (Start == start):
                clear()
                print("Wait.....")
                time.sleep(1)
                clear()
                print("==============================================================================================")
                print("Periodic Table Ver 1.4.7-------Made By JWare Soft Development Team")
                print("Copyright ⓒ JWare Soft Develoment Team 2019")
                print("If you are new in this program, enter \"help\", \"info\", \"copyright\" for more informations")
                print("you can checked the updated contents. type \"updated\"")
                print("※!!!!!BEFORE USING THIS PROGRAM PLEASE TYPE \"manual\"!!!!!※")
                print("If you want to quit this program, type quit and Press Enter")
                print("==============================================================================================")
                break;
    if (cse == "question"):
        question()
    if (cse == "manual"):
        manual()

    if(cse != "H" and cse !="He" and cse !="Li" and cse !="Be" and cse !="B"
    and cse !="C" and cse !="N"and cse !="O" and cse !="F" and cse !="Ne" and cse !="Na"
    and cse !="Mg" and cse !="Al" and cse !="Si" and cse !="P" and cse !="S" and cse !="Cl" and cse !="Ar"
    and cse !="K" and cse !="Ca" and cse !="help" and cse !="copyright" and cse !="info" and cse !="quit"
    and cse !="Sc" and cse !="Ti" and cse !="V" and cse !="Cr" and cse !="Mn" and cse !="Fe" and cse !="Co"
    and cse !="Ni"  and cse !="Cu" and cse !="Zn" and cse !="Ga" and cse !="Ge" and cse !="As" and cse !="Se"  and cse !="Br" and cse !="Kr"
    and cse !="Rb" and cse !="Sr" and cse !="Y" and cse !="Zr" and cse !="clear" and cse !="updated" and cse !="question"
    and cse !="manual" and cse !="0704" and cse !="reload" and cse !="Nb" and cse !="Mo" and cse !="Tc" and cse !="Ru" and cse !="Rh"
    and cse !="Pd" and cse !="Ag" and cse !="Cd" and cse !="In" and cse !="Sn" and cse !="h" and cse !="he" and cse !="li" and cse != "be" and cse !="b" and cse !="c"
    and cse !="n" and cse !="o" and cse !="f" and cse !="ne" and cse !="na" and cse !="mg" and cse !="al" and cse !="si" and cse !="p" and cse !="s"
    and cse !="ar" and cse !="k" and cse !="ca" and cse !="sc" and cse !="ti" and cse !="v" and cse !="cr" and cse !="mn" and cse != "fe" and cse !="co"
    and cse !="ni" and cse !="cu" and cse !="zn" and cse !="ga" and cse !="ge" and cse !="as" and cse !="se" and cse !="br" and cse !="kr"
    and cse !="rb" and cse !="sr" and cse !="y" and cse !="zr" and cse !="nb" and cse !="mo" and cse !="tc" and cse !="ru" and cse !="rh" and cse !="pd"
    and cse !="ag" and cse !="cd" and cse !="in" and cse !="sn"):
        print("NameError: name '%s' is not defined" % cse)
        print("please check your Spelling")
        print("check the manual\n")
input()
