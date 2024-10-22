#Crie um programa que analisa uma lista de produtos e envie instruçoes para aquipe de estoque
#dizendo quai produtos devem ser enviados para a area de bebidas alcolicas 

""" 
1 - percorrer cada produto da lista 
2 - pra cada porduto, verificar se e alcolico 
3 - se for bebida alcolica, exibir a mensagem 'enviar ...' 
"""

def alcolico(bebida): 
    bebida = bebida.upper() 
    if 'BEB' in bebida:
        return True
    else: 
        return False

produtos = ['BEB523', 'TFA234', 'BEB946', 'bsa023', 'tfa194', 'bsa012', 'beb012', 'BEB4573', 'BEB943'] 

for produto in produtos:  
    if alcolico(produto):
        print(f'Enviar {produto} para setor de bebidas')
