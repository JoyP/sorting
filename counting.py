def countingSort(input, max):
    count = {}

    #needs inital value
    for index in range(max + 1):
        count[index] = 0

    for x in input:
        count[x] += 1

    total = 0

    for i in range(max + 1):
         for p in range(count[i]):
            input[total] = i
            total += 1

    return input


testArray = [9, 3, 1, 1, 3, 8, 9, 10, 12, 40, 20, 40]

print(countingSort(testArray, 40))