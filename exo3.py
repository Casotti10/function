preco = 3000
custo = 2000
lucro = 680

def calcular_imposto(preco, custo, lucro):
    imposto = preco - custo - lucro 
    carga = imposto / preco * 100
    return carga

print (f'{calcular_imposto(preco, custo, lucro):.0f}%')