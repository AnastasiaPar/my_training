first = int(input('введите число: '))
second = int(input('введите второе число: '))
third  = int(input('введите тетье число: '))
if  first == second == third:
    print(3)
elif first == second or first == third or third == second:
    print(2)
else:
    print(0)
