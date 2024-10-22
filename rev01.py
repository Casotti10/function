'''
def nome_funçao():      
    faça alguma coisa
    faça alguma coisa
    return valor_final
''' 
def cadastrar_produto():
    lista_produtos = []
    while True:
        produto = input('Nome do produto:')
        produto = produto.lower().strip() #Corrige a formatação
        if produto == 'sair': #Encerra o loop apos digitar a palavra 'sair'
            break  
        lista_produtos.append(produto) #adiciona o produto na lista
    return lista_produtos  #retorna a lista quando o laço termina

lista_produtos = cadastrar_produto() #chama a função e armazena lista de produtos
print(lista_produtos) #imprime a liista