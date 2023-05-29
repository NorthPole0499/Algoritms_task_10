def bin_find(data, elem):
    left, right = -1, len(data)
    while right - left > 1:
        middle = (left + right) // 2
        if elem > data[middle]:
            left = middle
        elif elem < data[middle]:
            right = middle
        else:
            return True, middle
    return False, 0


m, n = map(int, input('Введите размеры матрицы MxN через пробел: ').split())
matrix = []
for i in range(m):
    matrix.append(list(map(int, input(f'Введите элементы {i + 1} строки матрицы по возрастанию через пробел: ').split())))

x = int(input('Введите искомый элемент матрицы: '))

flag = True
for i in range(m):
    if matrix[i][0] <= x <= matrix[i][-1]:
        flg, index = bin_find(matrix[i], x)
        if flg:
            print(i + 1, index + 1)
            flag = False
            break
if flag:
    print(-1, -1)
