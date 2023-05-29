def ans_generator(data):
    if data[0] == 1:
        return "Победили крестики!"
    else:
        return "Победили нолики!"


print('1 - крестики, 0 - нолики')
print("Введите законченное поле в строку ввода по одной строчки.")
print("Значки вводите через пробел, после каждых трёх нажмите кнопку Enter")
first_row = list(map(int, input().split()))
second_row = list(map(int, input().split()))
third_row = list(map(int, input().split()))
num_of_cross = first_row.count(1) + second_row.count(1) + third_row.count(1)
num_of_null = first_row.count(0) + second_row.count(0) + third_row.count(0)

if num_of_null == num_of_cross - 1 or num_of_cross == num_of_null - 1:
    if len(first_row) == len(second_row) == len(third_row) == 3:
        if len(set(first_row)) == 1:
            print(ans_generator(first_row))
        elif len(set(second_row)) == 1:
            print(ans_generator(second_row))
        elif len(set(third_row)) == 1:
            print(ans_generator(third_row))
        elif first_row[0] == second_row[1] == third_row[2]:
            print(ans_generator(first_row))
        elif first_row[2] == second_row[1] == third_row[0]:
            print(ans_generator(third_row))
        elif len({first_row[0], second_row[0], third_row[0]}) == 1:
            print(ans_generator(first_row[:1]))
        elif len({first_row[1], second_row[1], third_row[1]}) == 1:
            print(ans_generator(first_row[1:2]))
        elif len({first_row[2], second_row[2], third_row[2]}) == 1:
            print(ans_generator(first_row[2:]))
        else:
            print("Ничья!")
    else:
        print("Неверный ввод данных!")
else:
    print("Неверное количество крестиков и ноликов!")
