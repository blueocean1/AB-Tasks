def count_sheeps(arrayOfSheeps):
    counter = 0
    for i in range(len(arrayOfSheeps)):
        if arrayOfSheeps[i]:
            counter += 1
    return counter
