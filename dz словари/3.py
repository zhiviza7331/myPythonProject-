a = {}
b = list()
while True:
    track = input('Трек: ')
    if track == 'off':
        break
    name = input('Имя: ')
    if name == 'off':
        break
    b.append(name)
    place = input('Место: ')
    if place == 'off':
        break
    b.append(place)
    a[tuple(b)] = track
print(a)