import os

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def salvar_fibonacci(n, caminho_arquivo):
    fib_sequence = fibonacci(n)
    with open(caminho_arquivo, 'w') as arquivo:
        for numero in fib_sequence:
            arquivo.write(f"{numero}\n")

def salvar_fatorial(n, caminho_arquivo):
    with open(caminho_arquivo, 'w') as arquivo:
        for i in range(1, n + 1):
            arquivo.write(f"{i}! = {fatorial(i)}\n")

def main():
    try:
        n = int(input("Digite um número inteiro positivo: "))
        if n <= 0:
            raise ValueError("O número deve ser maior que zero.")
    except ValueError as e:
        print(f"Erro: {e}")
        return
    
    caminho_fibonacci = 'fibonacci.txt'
    caminho_fatorial = 'fatorial.txt'
    
    salvar_fibonacci(n, caminho_fibonacci)
    salvar_fatorial(n, caminho_fatorial)
    
    print(f"Os primeiros {n} números da sequência de Fibonacci foram salvos em {os.path.abspath(caminho_fibonacci)}")
    print(f"Os fatoriais de 1 a {n} foram salvos em {os.path.abspath(caminho_fatorial)}")

if __name__ == "__main__":
    main()
