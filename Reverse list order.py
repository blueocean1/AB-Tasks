def r_list(lis_t):
    new_list = []
    for i in range(1, len(lis_t) + 1):
        new_list.append(lis_t[-i])
    return new_list


l = [1, 2, 3, 4, 5]
print(r_list(l))
