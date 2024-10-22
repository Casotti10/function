''' 
Crie um programa que analisa uma lista de produtos e envie instruçoes para aquipe de estoque
dizendo qual produtos devem ser enviados para a area de bebidas alcolicas 
---------------------------------------------------------------------
1 - percorrer cada produto da lista 
2 - pra cada porduto, verificar se e alcolico 
3 - se for bebida alcolica, exibir a mensagem 'enviar ...' 
'''
def eh_da_categoria(bebida, cod_categoria): #função para verificar se o cod_categoria esta dentro da bebida 
    bebida = bebida.upper()
    if cod_categoria in bebida:  
        return True 
    else:
        return False
    
produtos = ['BEB523', 'BSA234', 'BEB946', 'BSA023', 'tfa194', 'bsa012', 'beb012', 'BEB4573', 'BEB943'] 

for produto in produtos:  #Condição se a bebida alcolica e nao alcolica estiver dentro da categoria 
    if eh_da_categoria(produto, 'BEB'): #iteraçao da fuunçao com o codigo
        print(f'Enviar {produto} para o setor de bebidas ALCOOLICAS')    #printar alguma coisa.
    elif eh_da_categoria(produto, 'BSA'):
        print(f'Enviar {produto} para o setor de NAO ALCOOLICO')
   