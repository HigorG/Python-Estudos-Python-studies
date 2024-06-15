def escrever_numeros_no_arquivo(caminho_arquivo, numeros):
    with open(caminho_arquivo, 'w') as arquivo:
        for numero in numeros:
            arquivo.write(f"{numero}\n")

def ler_e_totalizar_numeros_do_arquivo(caminho_arquivo):
    total = 0
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            numero = int(linha.strip())
            print(numero)
            total += numero
    return total

caminho_arquivo = r'C:\Users\Higor\Desktop\inteiros.txt'


numeros = [1, 2, 3, 4, 5, 6]

escrever_numeros_no_arquivo(caminho_arquivo, numeros)


total = ler_e_totalizar_numeros_do_arquivo(caminho_arquivo)


print(f"Total: {total}")
