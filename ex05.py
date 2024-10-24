vendas = {
    'VE001' : (15000, 'Concluido', ''),
    'VE002' : (13300, 'Cancelada pelo Cliente', ''),
    'VE003' : (12000, 'Concluido', ''),
} 

vendas = {'VE001':(9868, 'Concluido'), 'VE002':(9642, 'Concluido'),'VE003':(6007, 'Concluido'), 'VE004':(15562, 'Cancelado', 'Estoque em falta'), 'VE005':(15562, 'Cancelado', 'Cancelado pelo cliente')} 

def vendas(dicionario_vendas): 
    numerador = 0 
    denominador = 0 
    for venda in dicionario_vendas:
        valor,status, motivo = dicionario_vendas[venda] 
        if status == 'Concluido':
            denominador += valor 
        elif status
            