def multiples_3_or_5(lis_t):
    suma = 0
    for i in lis_t:
        if i % 3 == 0 or i % 5 ==0:
            suma += i
    return suma


lis_t = [x for x in range(10)]
print(lis_t)
s = multiples_3_or_5(lis_t)
print(s)
