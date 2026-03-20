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

# La condición if len(sys.argv) == 0 nunca se cumplirá porque sys.argv siempre tiene al menos un elemento (el nombre del script). Debes verificar que haya 2 argumentos (el script + el número).

if len(sys.argv) < 2:
   print("Debe informar un número o rango (ej. 4-8, -10, 5-)!")
   sys.exit()

# Verificar si el argumento contiene un guión (rango)
if '-' in sys.argv[1]:
    # Procesar rango
    partes = sys.argv[1].split('-')
    
    # Caso "-hasta" (ej. -10)
    if partes[0] == '':
        fin = int(partes[1])
        inicio = 1
        print(f"Calculando factoriales desde {inicio} hasta {fin}:")
        for num in range(inicio, fin + 1):
            print("Factorial ", num, "! es ", factorial(num))
    
    # Caso "desde-" (ej. 5-)
    elif partes[1] == '':
        inicio = int(partes[0])
        fin = 60
        print(f"Calculando factoriales desde {inicio} hasta {fin}:")
        for num in range(inicio, fin + 1):
            print("Factorial ", num, "! es ", factorial(num))
    
    # Caso rango normal "desde-hasta"
    else:
        inicio = int(partes[0])
        fin = int(partes[1])
        
        if inicio > fin:
            print("El número inicial debe ser menor o igual al final")
            sys.exit()
        
        print(f"Calculando factoriales desde {inicio} hasta {fin}:")
        for num in range(inicio, fin + 1):
            print("Factorial ", num, "! es ", factorial(num))
else:
    # Procesar número único
    num = int(sys.argv[1])
    print("Factorial ", num, "! es ", factorial(num))