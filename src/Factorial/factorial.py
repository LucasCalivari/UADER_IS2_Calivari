#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    #Función que calcula el factorial de un número
   # Parámetro: num - número entero a calcular su factorial
    #Retorna: el factorial calculado o 0 si es negativo
    # Verificar si el número es negativo
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    # El factorial de 0 es 1 por definición
    elif num == 0: 
        return 1
        
    else: 
        # Inicializar el factorial en 1
        fact = 1
        # Bucle while para multiplicar desde num hasta 2
        while(num > 1): 
            fact *= num   # Multiplicar el factorial actual por el número
            num -= 1      # Decrementar el número para la siguiente iteración
        return fact 

# Verificar que se haya proporcionado al menos un argumento
# sys.argv[0] contiene el nombre del script, por eso verificamos longitud < 2
if len(sys.argv) < 2:
   print("Debe informar un número o rango (ej. 4-8, -10, 5-)!")
   sys.exit()  # Salir del programa si no hay argumentos

# Verificar si el argumento contiene un guión para determinar si es un rango
if '-' in sys.argv[1]:
    # Dividir el argumento en dos partes usando el guión como separador
    # Ejemplos: "4-8" -> ["4", "8"], "-10" -> ["", "10"], "5-" -> ["5", ""]
    partes = sys.argv[1].split('-')
    
    # Caso 1: Formato "-hasta" (ejemplo: -10)
    # Cuando la primera parte está vacía, significa que no hay límite inferior
    if partes[0] == '':
        # Convertir la segunda parte a entero (el límite superior)
        fin = int(partes[1])
        # Establecer el límite inferior como 1
        inicio = 1
        print(f"Calculando factoriales desde {inicio} hasta {fin}:")
        # Bucle para calcular factorial de cada número en el rango
        for num in range(inicio, fin + 1):
            print("Factorial ", num, "! es ", factorial(num))
    
    # Caso 2: Formato "desde-" (ejemplo: 5-)
    # Cuando la segunda parte está vacía, significa que no hay límite superior
    elif partes[1] == '':
        # Convertir la primera parte a entero (el límite inferior)
        inicio = int(partes[0])
        # Establecer el límite superior como 60
        fin = 60
        print(f"Calculando factoriales desde {inicio} hasta {fin}:")
        # Bucle para calcular factorial de cada número en el rango
        for num in range(inicio, fin + 1):
            print("Factorial ", num, "! es ", factorial(num))
    
    # Caso 3: Formato normal "desde-hasta" (ejemplo: 4-8)
    # Ambas partes tienen valores
    else:
        # Convertir ambas partes a enteros
        inicio = int(partes[0])
        fin = int(partes[1])
        
        # Validar que el inicio sea menor o igual al final
        if inicio > fin:
            print("El número inicial debe ser menor o igual al final")
            sys.exit()
        
        print(f"Calculando factoriales desde {inicio} hasta {fin}:")
        # Bucle para calcular factorial de cada número en el rango
        for num in range(inicio, fin + 1):
            print("Factorial ", num, "! es ", factorial(num))
else:
    # Caso 4: Número único (sin guión)
    # Convertir el argumento a entero
    num = int(sys.argv[1])
    # Calcular y mostrar el factorial del número único
    print("Factorial ", num, "! es ", factorial(num))