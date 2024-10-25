#EXCESSOES TRY E EXCEPTION

def servidor (email):
    try: #
        posicao = email.index('@')  # Encontra a posição do '@'
    except:#Se nao tiver o @ o codigo da um erro
        raise ValueError('Email digitado nao tem @. Digite novamente') 
    else:#Se nao acontecer o erro esperado ele roda o restante do codigo
        servidor = email[posicao:] # Extrai a substring a partir do '@'
        if 'gmail' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor or 'outlook' in servidor:\
            return 'hotmail' 
        elif 'yahoo' in servidor:
            return 'yahoo'
        else:
            return 'Servidor nao encontrado' 
    
email = input('Qual é seu email?: ')
print(servidor(email))