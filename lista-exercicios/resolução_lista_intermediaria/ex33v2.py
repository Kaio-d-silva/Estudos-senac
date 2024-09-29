import time
import matplotlib.pyplot as plt

# Função recursiva para calcular Fibonacci
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Função iterativa para calcular Fibonacci
def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Função para medir o tempo de execução
def medir_tempo(funcao, n):
    inicio = time.time()
    resultado = funcao(n)
    fim = time.time()
    return fim - inicio

# Programa principal
def main():
    valores_n = list(range(10, 31, 2))  # Valores de n de 10 a 30, em passos de 2
    tempos
