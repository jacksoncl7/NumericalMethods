asterisco = int(input('quantos asteriscos vc quer meu bom?'))
resp = []
for n in range(asterisco):
    resp.append('*')
print(resp)

resp = []
while asterisco > 0:
    resp.append('*')
    asterisco -= 1
print(resp)
