print("введите трёхзначное число:")
number = int(input())
a = number // 100
b = number % 100
c = number % 10
print(a + (b // 10) + c)
