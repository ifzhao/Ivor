def get_jiecheng(number):
    result = 1
    while number > 0:
        result*=number
        number-=1
    return result


print(get_jiecheng(6))
print(get_jiecheng(3))
print(get_jiecheng(100))