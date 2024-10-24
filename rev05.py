#retornar um numero
def minha_soma(a, b):
    return a + b
soma = minha_soma(1, 2)
print(soma) 

#retornar um texto
def padronizar_texto(texto):
    texto = texto.strip() # Remove espaços em branco no início e no fim
    texto = texto.casefold()  # Converte o texto para minúsculas
    texto = texto.replace('   ', ' ') # Remove ocorrências de três espaços
    return texto 
nova_variavel = padronizar_texto('SalVe   GalEra' )
print(nova_variavel) 

#returnar uma boolean 

def minhas_metas(venda, meta):
    if venda >= meta:
        return True 
    else:
        return False

venda_jose = 100
meta = 300 

if minhas_metas(venda_jose, meta):
    print('Jose bateu a meta')
else:
    print('Jose nao bateu a meta') 

#Retornar uma lista, tupla ou dicionario
def filtrar_lista_texto(lista, pedaço_texto):
    lista_filtrada = []
    for item in lista: #Um loop for é iniciado. Ele percorre cada item da lista.
        if pedaço_texto in item: #Para cada item, verifica-se se o pedaço_texto está presente dentro do item
            lista_filtrada.append(item) #Adiciona o item dentro da lista
    return lista_filtrada

lista_textos = ['lucas@gmail.com', 'marina@hotmail.com', 'juca@gmail.com']   
lista = filtrar_lista_texto(lista_textos, 'hotmail') #atribui a variavel a funçao
print(lista)
     