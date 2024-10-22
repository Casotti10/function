def area(largura, comprimento): 
    a = largura * comprimento 
    print(f'A area de um terreno {largura}x{comprimento} é de {area}m')
    
    
print('Controle de Terrenos')
print('=-' *30)
l = float(input('Largura (m): '))
c = float(input('Comprimento(m): ' )) 
area(l,c)