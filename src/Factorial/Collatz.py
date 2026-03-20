
# Calcula la conjetura de Collatz para números entre 1 y 10000           
# Genera gráfico simple de iteraciones vs número inicial   
import matplotlib.pyplot as plt

def collatz_iteraciones(n):
    iteraciones = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iteraciones += 1
    return iteraciones

# Calcular para números del 1 al 10000
numeros = list(range(1, 10001))
iteraciones = [collatz_iteraciones(n) for n in numeros]

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.scatter(iteraciones, numeros, s=1, c='blue', alpha=0.5)
plt.xlabel('Número de iteraciones')
plt.ylabel('Número inicial (n)')
plt.title('Conjetura de Collatz (números 1 a 10000)')
plt.grid(True, alpha=0.3)
plt.savefig('collatz_grafico.png', dpi=150)
plt.show()