#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                        *
#* calcula el factorial de un número usando programación orientada a objetos*
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    """
    Clase para calcular factoriales usando programación orientada a objetos
    """
    
    def __init__(self):
        """
        Constructor de la clase Factorial
        Inicializa la instancia sin parámetros adicionales
        """
        pass
    
    def factorial(self, num):
        """
        Método  que calcula el factorial de un número
        Parámetro: num - número entero a calcular su factorial
        Retorna: el factorial calculado o 0 si es negativo
        """
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
    
    def run(self, min_num, max_num):
        """
        Método principal que calcula y muestra los factoriales entre min_num y max_num
        Parámetros: 
            min_num - límite inferior del rango
            max_num - límite superior del rango
        """
        # Validar que el mínimo sea menor o igual al máximo
        if min_num > max_num:
            print("El número mínimo debe ser menor o igual al máximo")
            return
        
        print(f"Calculando factoriales desde {min_num} hasta {max_num}:")
        # Bucle para calcular factorial de cada número en el rango
        for num in range(min_num, max_num + 1):
            print("Factorial ", num, "! es ", self.factorial(num))

def main():
    """
    Función principal que procesa los argumentos de línea de comandos
    y ejecuta el cálculo de factoriales usando la clase Factorial
    """
    # Verificar que se haya proporcionado al menos un argumento
    if len(sys.argv) < 2:
        print("Debe informar un número o rango (ej. 4-8, -10, 5-)!")
        sys.exit()
    
    # Crear una instancia de la clase Factorial
    calculadora = Factorial()
    
    # Verificar si el argumento contiene un guión para determinar si es un rango
    if '-' in sys.argv[1]:
        # Dividir el argumento en dos partes usando el guión como separador
        partes = sys.argv[1].split('-')
        
        # Caso 1: Formato "-hasta" (ejemplo: -10)
        if partes[0] == '':
            fin = int(partes[1])
            inicio = 1
            calculadora.run(inicio, fin)
        
        # Caso 2: Formato "desde-" (ejemplo: 5-)
        elif partes[1] == '':
            inicio = int(partes[0])
            fin = 60
            calculadora.run(inicio, fin)
        
        # Caso 3: Formato normal "desde-hasta" (ejemplo: 4-8)
        else:
            inicio = int(partes[0])
            fin = int(partes[1])
            calculadora.run(inicio, fin)
    else:
        # Caso 4: Número único (sin guión)
        num = int(sys.argv[1])
        # Para número único, calcular desde 1 hasta el número
        calculadora.run(1, num)

# Punto de entrada del programa
if __name__ == "__main__":
    main()