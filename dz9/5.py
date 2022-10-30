def F(cal, a, **coll):
    print(f'{cal}: {a}')
    for i in coll:
        print(f'{i}: {coll[i]}')