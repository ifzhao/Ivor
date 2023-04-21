def get_jiechang(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result


print("jiechang 6 = ",get_jiechang(6))
print("jiechang 3 = ",get_jiechang(3))
print("jiechang 100 = ",get_jiechang(100))