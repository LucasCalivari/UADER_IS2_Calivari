#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

 #La condición if len(sys.argv) == 0 nunca se cumplirá porque sys.argv siempre tiene al menos un elemento (el nombre del script). Debes verificar que haya 2 argumentos (el script + el número).

if len(sys.argv) < 2:
   print("Debe informar un número!")
   sys.exit()
num=int(sys.argv[1])
print("Factorial ",num,"! es ", factorial(num)) 

