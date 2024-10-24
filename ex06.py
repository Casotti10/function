clientes_devedores = [
    ("12345678901", 1200, 25),  # CPF, Valor devido, Dias
    ("98765432100", 500, 15),
    ("11223344556", 2000, 5),
    ("22334455667", 1400, 20),
    ("33445566778", 3000, 23),
] 

def clientes_negativos(lista_devedores):
    lista_negativa = []
    for cliente in lista_devedores:
        cpf, valor, dias = cliente
        if valor > 1000 and dias > 20:
            lista_negativa.append(cpf)
    return lista_negativa

devedores = clientes_negativos(clientes_devedores)
print(f'Os CPF negativos sao: {devedores}') 
print(f'O total de CPF NEGATIVADOS sao: {len(devedores)} ')