N = int(input("Input an 4-digit integer: "))
n_1 = N // 1000
n_2 = (N % 1000) // 100
n_3 = (N % 100) // 10
n_4 = N % 10
multiplication = n_1 * n_2 * n_3 * n_4
print("Multiplication of digits = ", multiplication)
l = [n_1, n_2, n_3, n_4]
print("reversed_number", end=": ")
l.reverse()
for i in range(len(l)):
    print(l[i], end='')
l.sort()
print("\nsorted number", end=': ')
for i in range(len(l)):
    print(l[i], end='')
