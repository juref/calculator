#!/usr/bin/env python
# -*- coding: utf-8 -*-

class textColor:
    RESET = '\033[0m'
    BOLD = '\033[01m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'
    BLACK = '\033[90m'

from decimal import Decimal
import random
from os import system

skrita_stevilka = round(random.uniform(1, 30))
print textColor.BLACK + "\nZa lažje ugibanje, " + str(skrita_stevilka).rstrip('0').rstrip('.') + " je skrita številka." + textColor.RESET  if '.' in str(skrita_stevilka) else str(skrita_stevilka) + " je skrita številka." + textColor.RESET

while True:
    odgovor = int(raw_input("\nUgani skrito številko med 1 in 30: "))

    if odgovor == skrita_stevilka:
        # system('clear')  # dela samo v terminalu za mac in linux!!!
        print textColor.BOLD + textColor. GREEN + "\nČestitamo, " + str(skrita_stevilka).rstrip('0').rstrip('.') + " je pravilni odgovor!" + textColor.RESET if '.' in str(skrita_stevilka) else str(skrita_stevilka) + "je pravilni odgovor!" + textColor.RESET
        break
    else:
        # system('clear') # dela samo v terminalu za mac in linux!!!
        print textColor.ORANGE + "\nŽal " + str(odgovor) + " ni pravilen odgovor. Prosim poiskusite ponovno!" + textColor.RESET


str(skrita_stevilka).rstrip('0').rstrip('.') if '.' in str(skrita_stevilka) else str(skrita_stevilka)