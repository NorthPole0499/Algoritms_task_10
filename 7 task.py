from random import randint

nums = list(set([randint(0, 100) for _ in range(randint(10, 20))]))
print("Имеющийся массив:", nums)
min_n, max_n = min(nums), max(nums)
flags = [False for _ in range(max_n - min_n)]
for x in nums:
    flags[x - min_n - 1] = True
for i in range(len(flags)):
    if not flags[i]:
        print("Минимальное пропущенное число:", min_n + i + 1)
        break
