import time

def contador(inicio, fim, passo): 
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio <= fim:
        cont  = inicio
        while cont <= fim:
            print(f'{cont}', end= ' ')
            time.sleep(0.5)
            cont += passo
        print('FIM') 
    else:
        cont = inicio 
        while cont >= fim: 
            print(f'{cont}', end= ' ')
            time.sleep(0.5)
            cont -= passo 
        print('Fim')
            
contador(1, 10, 1)
contador(10,0, 1)