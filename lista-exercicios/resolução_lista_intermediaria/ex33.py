import time

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
    funcao(n)
    fim = time.time()
    return fim - inicio

# Comparando o tempo de execução
def comparar_tempos(max_n):
    print(f"{'N':<5} {'Recursivo (s)':<20} {'Iterativo (s)':<20}")
    print("-" * 45)
    
    for n in range(max_n):
        tempo_recursivo = medir_tempo(fibonacci_recursivo, n)
        tempo_iterativo = medir_tempo(fibonacci_iterativo, n)
        
        print(f"{n:<5} {tempo_recursivo:<20.6f} {tempo_iterativo:<20.6f}")

# Programa principal
max_n = 30  # Limite superior para n (não muito alto devido ao tempo de execução do recursivo)
comparar_tempos(max_n)
