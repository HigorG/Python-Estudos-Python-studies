
caminho_arquivo = r'C:\Users\Higor\Desktop\preco.txt'



def processar_lista_compras(caminho_arquivo):
    total_compra = 0
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            if ";" in linha:
                nome_produto, quantidade, preco_unitario = linha.strip().split(";")
                quantidade = int(quantidade)
                preco_unitario = float(preco_unitario)
                total_item = quantidade * preco_unitario
                print(f"Produto: {nome_produto}, Quantidade: {quantidade}, Preço Unitário: {preco_unitario:.2f}, Total: {total_item:.2f}")
                total_compra += total_item
    print(f"Total da compra: {total_compra:.2f}")


conteudo_compras = """maçã;2;3.50
banana;5;1.20
arroz;1;20.00
feijão;3;7.50"""

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write(conteudo_compras)

processar_lista_compras(caminho_arquivo)
