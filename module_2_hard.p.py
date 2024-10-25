def gess_password(number):
    password = ""
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += f'{i}{j}'
    return password

n = int(input('Введите целое число от 3 до 20: '))
if 3 <= n <= 20:
    result = gess_password(n)
    print(f'Пароль для числа {n}:', result)
else:
    print('Число не входит в диапазон от 3 до 20 ')






