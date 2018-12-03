#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

class textColor:
    RESET = '\033[0m'
    BOLD = '\033[01m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'

from decimal import Decimal


prvo_stevilo = None
while True:
    prvo_stevilo = raw_input("Vnesite prvo število: ")
    if not prvo_stevilo.isalpha(): break
    else:
        print "\033[91mTo ni število\033[0m"

operacija = None
while True:
    operacija = raw_input("Vnesi željeno funkcijo (+, -, * ali /): ")
    if operacija in ("+", "-", "*", "/"): break
    else:
        print "\033[91mNepoznana funkcija\033[0m"

drugo_stevilo = None
while True:
    drugo_stevilo = raw_input("Vnesite drugo število: ")
    if not drugo_stevilo.isalpha(): break
    else:
        print "\033[91mTo ni število\033[0m"


if operacija == "+":
    vsota = float(prvo_stevilo) + float(drugo_stevilo)
    print textColor.GREEN + textColor.BOLD + str(prvo_stevilo) + " + " + str(drugo_stevilo) + " = " + (str(round(vsota, 3))).rstrip('0').rstrip('.') if '.' in (str(round(vsota, 3))) else (str(round(vsota, 3)))


elif operacija == "-":
    razlika = float(prvo_stevilo) - float(drugo_stevilo)
    print textColor.GREEN + textColor.BOLD + str(prvo_stevilo) + " - " + str(drugo_stevilo) + " = " + (str(round(razlika, 3))).rstrip('0').rstrip('.') if '.' in (str(round(razlika, 3))) else (str(round(razlika, 3)))

elif operacija == "*":
    kolicnik = float(prvo_stevilo) * float(drugo_stevilo)
    print textColor.GREEN + textColor.BOLD + str(prvo_stevilo) + " * " + str(drugo_stevilo) + " = " + (str(round(kolicnik, 3))).rstrip('0').rstrip('.') if '.' in (str(round(kolicnik, 3))) else (str(round(kolicnik, 3)))


elif operacija == "/":
    ulomek = float(prvo_stevilo) / float(drugo_stevilo)
    print textColor.GREEN + textColor.BOLD + str(prvo_stevilo) + " / " + str(drugo_stevilo) + " = " + (str(round(ulomek, 3))).rstrip('0').rstrip('.') if '.' in (str(round(ulomek, 3))) else (str(round(ulomek, 3)))

else:
    print "Neznana funkcija!"