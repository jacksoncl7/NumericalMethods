perfect_square = int(input('input perfect number: '))
validator = True
iterator = 3
total = 1
while validator:
    if total > perfect_square:
        print('Error')
        break
    elif perfect_square == total:
        print('Perfect')
        break

    total += iterator
    iterator += 2
