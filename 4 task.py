def walk(c):
    global n
    if c > n:
        return 0
    elif c == n:
        return 1
    else:
        return walk(c + 1) + walk(c + 2) + walk(c + 3)


n = int(input())
print("Количество возможных вариантов:", walk(0))
