import tkinter
from tkinter import *

#Nome da guia e dimenções;
telaMain = tkinter.Tk(className=" MERCADO")
telaMain.geometry('400x700')

#Abre arquivo de catálogo e lê somente à partir da linha 2;
arquivo = open('catalogo.txt','r',encoding='utf8')
catalogo = arquivo.readlines()[2:]
arquivo.close()

#lista de compras;
lista_compras = []

#Quando ativado, adiciona item na lista e exibe no terminal;
def pressiona(item):
    print("Item adicionado: ", str(mercado.get(ACTIVE)))
    lista_compras.append(str(mercado.get(ACTIVE).strip('\n')))

#Ao clickar em sair do mercado, sua lista é exibida no terminal e salva em um arquivo externo;
def sair():
    print("Sua lista de compras é: ", lista_compras)
    arquivo = open('lista.txt','w',encoding='utf8')
    arquivo.writelines("#SUA LISTA DE COMPRAS:\n\n")
    arquivo.writelines('\n'.join(lista_compras))
    arquivo.close()
    exit()

#Exibe na tela a lista de produtos disponíveis no mercado;
mercado = Listbox(telaMain)
for item in catalogo:
    mercado.insert(END,item)

#Define o tamanho da lista de produtos (varia de acordo com a quantidade de produtos);
mercado.configure(height=len(catalogo) if len(catalogo) < 40 else 40, width=30)

#Adiciona produto ao pressionar duas vezes sobre ele;
botao = mercado.bind('<Double-1>',pressiona)

#Encerra o programa;
sair = Button(text="Sair do mercado",command=sair)

#Carrega o sistema.
mercado.pack()
sair.pack()
telaMain.mainloop()
arquivo.close()
