entry = input('digite uma sequecia binaria: ex 1101 ')
aux = 0
resp = 0
for num in entry[::-1]:
    resp += int(num)*2**aux
    aux += 1

print(resp)
