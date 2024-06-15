# -*- coding: utf-8 -*-
"""
Created on Thu May 16 09:07:42 2024

@author: Higor
"""

texto = "Aula de tecnicas de programação II, Arquivos!"
lista = [1,2,3,4,5,6]
tupla = (1,2,3,4)
documentoAula = open(r'C:\Users\Higor\Desktop\aulaTPII.txt', "w")
documentoAula.write(str(lista)+"\n")
documentoAula.writelines(str(tupla)+"\n")
documentoAula.seek(10)
documentoAula.write(texto)
documentoAula.close()