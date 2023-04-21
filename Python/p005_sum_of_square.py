def sum_of_square(n):
    result = 0
    for number in range(1, n+1):
        result += number * number
    return result
print(sum_of_square(2))

