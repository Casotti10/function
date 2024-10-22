#Crie um programa que analisa uma lista de produtos e envie instruçoes para aquipe de estoque
#dizendo quai produtos devem ser enviados para a area de bebidas alcolicas 

""" 
1 - percorrer cada produto da lista 
2 - pra cada porduto, verificar se e alcolico 
3 - se for bebida alcolica, exibir a mensagem 'enviar ...' 
"""

def categoria(bebida,): 
    bebida = bebida.upper() 
    if cod_categoria in bebida:
        return True
    else: 
        return False

produtos = ['BEB523', 'BSA234', 'BEB946', 'BSA023', 'tfa194', 'bsa012', 'beb012', 'BEB4573', 'BEB943'] 

for produto in produtos:  
    if categoria(produto, 'BEB'):
        print(f'Enviar {produto} para setor de bebidas alcolicas')
    elif categoria (produto, 'BSA'):
        print(f'Enviar {produto} para setor de bebidas NAO alcolicas')