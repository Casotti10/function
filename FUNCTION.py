def padronizar_codigos(lista_codigo, padrao = 'm'):
    for i, item in enumerate(lista_codigo):
        item.replace('  ', ' ') # Reatribuir o valor após replace 
        item.strip() # Reatribuir o valor após strip
        if padrao == 'm':
            item = item.casefold() 
        elif padrao == 'M':
            item = item.upper() 
        lista_codigo[i] = item # Atualizar o item na lista
    return lista_codigo


cod_produtos = [' ABC321', 'abc123', 'AbC306']
print(padronizar_codigos(cod_produtos, 'M')) #Altera o valor padrao da lista mudando a letra 'M'

