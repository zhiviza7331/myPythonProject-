print("введите трёхзначное число:")
number = int(input())
a = number // 100
b = number % 100 // 10
c = number % 10
print(int(str(c) + str(b) + str(a)))