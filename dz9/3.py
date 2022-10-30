def b():
    a = input()
    if a != '':
        return int(a) + b()
    else:
        return 0
print(b())