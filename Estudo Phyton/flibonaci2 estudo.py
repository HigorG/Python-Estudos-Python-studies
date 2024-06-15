# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 21:06:58 2024

@author: Higor
"""

# Número para o qual você deseja calcular a sequência de Fibonacci
n = int(input("Digite um número para executar o cálculo de Fibonacci: "))

# Inicializando os primeiros dois números da sequência de Fibonacci
a, b = 0, 1

# Imprimindo os dois primeiros números da sequência
print(a)
print(b)

# Inicializando a variável para contar os termos gerados
cont = 2

# Calculando e imprimindo os próximos números da sequência até atingir o n-ésimo termo
while cont < n:
    c = a + b
    print(c, " (soma de", a, "e", b, ")")
    a, b = b, c
    cont += 1
