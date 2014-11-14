input = [1,5,3,7,6,2,9,3,5,6]
sorted = 0

def insSort(input, i, sorted):
    if sorted == len(input):
        return input
    elif input[i] >= input[i-1]:
        sorted += 1
        insSort(input, sorted, sorted)
    elif input[i] < input[i-1]:
        currentNum = input[i]
        input[i] = input[i-1]
        input[i-1] = currentNum

        insSort(input, i-1, sorted)

insSort(input, 1, 0)
print(input)
