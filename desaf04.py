from random import randint


def sorteio(lista): 
    for c in range(0, 5):
        n = randint(1, 5)
        lista.append(n)

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0: 
            soma +=  valor
    print(f'Somando os valore pares da {lista}, temos {soma} ')
         
         
numeros = []
sorteio(numeros)
print(numeros)
somapar(numeros) 
""" 
1 - criar uma lista chamada numeros 
2 - 2 funçoes chamadas sorteio() e somapar() 
3 - a primeira funçao vai sortear 5 numeros e colocar dentro de uma lista 
4 - a segunda funçao vai mostrar a soma entre todos os valores pares 
""" 