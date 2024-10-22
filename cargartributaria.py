#Crie uma function que calcule qual o % de carga tributaria que esta sendo aplicada 
#sobre um determinado produto, dado o preço de venda, o "lucro" 
# e os custos(com exceção do imposto) dele 
preco = 1500
custo = 400 
lucro = 800 

#função para calcular a carga tributaria 
def carga_trbituraria(preco, custo, lucro): 
    imposto = preco - custo - lucro # Calcula o valor do imposto
    carga = imposto / preco # Calcula a carga tributária em relação ao preço
    return carga  # Retorna a carga tributária como um valor decimal

# Exibindo o valor da carga tributária como porcentagem
print(f'A carga tributaria do produto foi de {carga_trbituraria(preco, custo, lucro):.2%}')
