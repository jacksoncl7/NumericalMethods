# para rodar basta digitar no terminal python3 ./nome_do_arquivo.py
num = int(input('numero na base 10: '))
base = 2
resp = ''

while num >= base:
    resp += str(num % base)
    num = num // base
resp += str(num)

print(resp[::-1])
