def ler_numeros_e_gravar():

    caminho_arquivo = r'C:\Users\Higor\Desktop\numeros_reais.txt'
    
   
    with open(caminho_arquivo, "w") as arquivo:
        while True:
            
            numero = float(input("Digite um número real (0 para sair): "))
            

            if numero == 0:
                break

            arquivo.write(f"{numero:.3f}\n")
    
    print(f"Os números foram gravados em {caminho_arquivo}")
ler_numeros_e_gravar()
