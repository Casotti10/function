def cadastrar_produto():
    produto = input('Nome do produto que deseja cadastrar: ') 
    produto = produto.lower() 
    return produto    

for i in range(2):
    var_produto = cadastrar_produto() 
    print(var_produto)

    
 