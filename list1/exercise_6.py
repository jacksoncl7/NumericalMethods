seq = list(map(int, input('digite a sequencia: ').split()))
aux = seq[0]
counter = 0
result = 0
for num in seq[1:]:
    if aux != num:
        counter = 0
    else:
        counter += 1

    if counter >= 2:
        result += 1
        
    aux = num
    #print("contador: {} numeral: {} resultado: {}".format(counter, num, result))
print(result)
