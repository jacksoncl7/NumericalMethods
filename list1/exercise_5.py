def percent(total, parcial):
    return int(round(parcial/total, 2) * 100)

dados = map(int, input('manda a sequencia do pente: ').split())
negativo, zero, positivo = 0, 0, 0
for dado in dados:
    if dado < 0:
        negativo += 1
    elif dado == 0:
        zero += 1
    else:
        positivo += 1

t = negativo + zero + positivo 
p_neg, p_zero, p_pos = percent(t, negativo), percent(t, zero), percent(t, positivo)

print("{}% negativos, {}% zeros e {}% positivos".format(p_neg, p_zero, p_pos))
