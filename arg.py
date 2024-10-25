#Ordem dos argumentos 
#Sempre os positional vem antes e depois os keywords 
#Sempre os argumentos individuais vem antes de depois os "multiplos"
#def exemplo(num1, num2, num3, *numero, 1, 2, 3)

def minha_funçao(*numeros, num1, num2):
    soma = 0 
    for numero in numeros:
        soma += numero
    soma += num1 + num2
    return soma 
print(minha_funçao(10, 2, num1= 1, num2=2))
