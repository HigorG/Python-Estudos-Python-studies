import random
import csv

def gerar_estoque(N, caminho_arquivo="Estoque.csv"):
    if N <= 10 or N >= 10000:
        raise ValueError("N deve ser maior que 10 e menor que 10.000")
    
    nomes_produtos = ["ProdutoA", "ProdutoB", "ProdutoC", "ProdutoD", "ProdutoE"]
    with open(caminho_arquivo, 'w', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo, delimiter=';')
        escritor_csv.writerow(["Codigo", "Nome", "Quantidade", "Preco", "ICMS"])
        for i in range(1, N + 1):
            codigo = i
            nome = random.choice(nomes_produtos)
            quantidade = random.randint(1, 100)
            preco = round(random.uniform(10.0, 100.0), 2)
            icms = round(preco * 0.18, 2)
            escritor_csv.writerow([codigo, nome, quantidade, preco, icms])



