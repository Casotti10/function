'''
No primeiro bloco de codigo fazemos uma função para analisar as bebidas alcolicas de uma lista de produtos
No segundo bloco de codigo no 'for' imprimos as bebidas alcolicas que etsoa dentro de uma lista 
'''

def ehalcolico(bebida):
    bebida = bebida.upper() #variavel criada dentro da função
    if 'BEB' in bebida:
        return True
    else:
        return False

produtos = ['bab022', 'BEB023', 'BEB076', 'bab102', 'BEB58'] 
for produto in produtos:
    if ehalcolico(produto):
        print(f'Enviar {produto} para o setor de bebidas alcolicos')

 


    