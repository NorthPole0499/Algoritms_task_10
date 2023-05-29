def exp_filter(data, y_k0, degree):
    if len(data) == 1:
        return y_k0 + degree * (data[0] - y_k0)
    else:
        return exp_filter(data[1:], y_k0 + degree * (data[0] - y_k0), degree)

data = list(map(int, input("Введите измеренные знначения: ").split()))
degree = float(input("Введите степень фильтрации от 0 до 1: "))
print(exp_filter(data, data[0], degree))
