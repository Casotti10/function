def cadastrar_produto(): 
    produto = input('Digite o nome do produto: ')
    produto = produto.lower()
    produto = produto.strip()
    produto = [produto]
    return produto

novo_produto = cadastrar_produto()
print(novo_produto)
