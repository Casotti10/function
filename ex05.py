vendas = {
    'VE001' : (15000, 'Concluido', ''),
    'VE002' : (13300, 'Cancelada pelo Cliente', ''),
    'VE003' : (12000, 'Concluido', ''),
} 

vendas = {'VE001':(9868, 'Concluido', ''), 'VE002':(9642, 'Concluido', ''),'VE003':(6007, 'Concluido', ''), 'VE004':(15562, 'Cancelado', 'Estoque em falta'), 'VE005':(15562, 'Cancelado', 'Cancelado pelo cliente')} 

def calculo_stockout(dicionario_vendas): 
    numerador = 0 
    denominador = 0 
    for venda in dicionario_vendas: #Esta linha inicia um loop que itera sobre cada venda no dicionário
        valor, status, motivo = dicionario_vendas[venda] #Para cada venda, a função desempacota os valores associados a essa venda em três variáveis: 
        if status == 'Concluido':
            denominador += valor 
        elif status == 'Cancelado' and motivo == 'Estoque em falta':
            denominador += valor
            numerador += valor
    return numerador / denominador 

print(f'{calculo_stockout(vendas):.2%}')