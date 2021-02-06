dados = map(int, input('manda a sequencia do pente: ').split())
negativo, zero, positivo = 0, 0, 0
for dado in dados:
    if dado < 0:
        negativo += 1
    elif dado == 0:
        zero += 1
    else:
        positivo += 1

print("{} negativos, {} zeros e {} positivos".format(negativo, zero, positivo))
