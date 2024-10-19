def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        a = []
        for j in range(m):
            a.append(value)
        matrix.append(a)
    return(matrix)
n = int(input("количество строк: "))
m = int(input("количество столбцов: "))
value = int(input("значения: "))
matrix = get_matrix(n, m, value)
print(matrix)








