def primo(num):
    if num <= 2:
        return True
    for i in range(3, num):
        if num % i == 0:
            return False
    return True

entry = int(input('digite um numero N e retornaremos os N primeiros primos: '))
solution = []
count = 1
while entry > 0:
    if primo(count):
        solution.append(count)
        entry -= 1
    count += 1
print(solution)
