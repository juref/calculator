#!/usr/bin/env python
# -*- coding: utf-8 -*-

class textColor:
    RESET = '\033[0m'
    BOLD = '\033[01m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'

from decimal import Decimal
import random

skrita_stevilka = round(random.uniform(0, 30))
print skrita_stevilka


while True:
    odgovor = int(raw_input("\nUgani skrito številko med 1 in 30: "))

    if odgovor == skrita_stevilka:
        print textColor.BOLD + textColor. GREEN + "\nČestitamo, " + str(skrita_stevilka).rstrip('0').rstrip('.') + " je pravilni odgovor!" if '.' in str(skrita_stevilka) else str(skrita_stevilka) + "je pravilni odgovor!"
        break
    else:
        print textColor.ORANGE + "\nŽal " + str(odgovor) + " ni pravilen odgovor. Prosim poiskusite ponovno!" + textColor.RESET
