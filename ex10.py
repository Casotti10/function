def minha_soma(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma
lista = minha_soma(1, 10)
print(lista) 

