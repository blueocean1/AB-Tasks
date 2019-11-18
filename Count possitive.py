arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
new_arr = []
counter = 0
sum_neg = 0
for i in arr:
    if i <= 0:
        sum_neg += i
    elif i > 0:
         counter += 1
new_arr.append(counter)
new_arr.append(sum_neg)
print(new_arr)


