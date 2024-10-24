meta = 10000
vendas = {
    'Lucas' : 25075,
    'Maria' : 5000,
    'João' : 30050,
    'Ana' : 12530,
    'Pedro' : 4000,
} 

def calculo_meta(meta, vendas):
    bateu_meta = []
    for vendedor in vendas:
        if vendas[vendedor] >= meta:
            bateu_meta.append(vendedor)
    percentual = len(bateu_meta) / len(vendas)
    return percentual, bateu_meta 

percent, meta_batida = calculo_meta(meta, vendas)


print(f'Vendas: {meta_batida}')
print(f'Percentual: {percent:.2%}')