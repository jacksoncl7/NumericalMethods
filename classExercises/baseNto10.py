# para rodar basta digitar no terminal python3 ./nome_do_arquivo.py
num, base = map(int, input('numero na base 10 e numero base: ').split())
resp = ''

while num >= base:
    resp += str(num % base)
    num = num // base
resp += str(num)

print(resp[::-1])
