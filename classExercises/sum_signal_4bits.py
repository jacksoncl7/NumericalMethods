# para rodar basta digitar  "python3 sum_signal_4bits.py" no terminal
# o dados de entrada devem seguir o seguinte exemplo
# entre com duas cadeias e um sinal na soma: 1000 - 0111
# onde o que deve ser digitado é: "1000 - 0111" ou qualquer dupla de binarios

def base2to10(string):
    aux = 0
    base10 = 0
    for num in string[:0:-1]:
        base10 += int(num)*2**aux
        aux += 1
    
    if string[0] == '0':
        return base10
    return base10 - 8
                
def twos_complement(stream):
    n_stream = ''
    for num in stream:
        n_stream += '0' if num == '1' else '1'

    if n_stream[-1] == '0':
        n_stream =  n_stream[:-1:] + '1'
    else:
       n_stream = sum_binary(n_stream, '0001') 

    return n_stream
        
def overflow(stream, flow=4):
    pass

def sum_binary(num1, num2, flow=4):
    new = ''
    over = 0
    for i in range(len(num1) - 1, -1, -1):
        result  = int(num1[i]) + int(num2[i])
        print('b: {} sum: {} over: {}'.format(new, result, over))
        if result == 2:
            if over == 0:
                over = 1
                new = '0' + new    
            else:
                new = '1' + new    
        elif result == 1:
            if over == 0:
                new = '1' + new
            else:
                new = '0' + new
        elif result == 0:
            if over == 0:
                new = '0' + new
            else:
                new = '1' + new
                over = 0
    return new


# Entrada
num1, s, num2 = input('entre com duas cadeias e um sinal na soma: ').split()
# Convertendo p/ b10
num1b10, num2b10 = base2to10(num1), base2to10(num2)
# Demonstrando os numeros b10
print('O na base 10 é: {} {} {}'.format(num1b10, s, num2b10))
# Executando o esperado
if s == '-':
    num2 = twos_complement(num2)
result = sum_binary(num1, num2)
print("A solução para a operação é: {} em binário e {} em decimal".format(result, base2to10(result)))
