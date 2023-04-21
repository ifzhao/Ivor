def get_even_number(begin, end):
    result = []
    for item in range(begin, end):
        if item % 2 == 0:
            result.append(item)
    return result


begin = 11
end = 23
print(f"begin={begin},end={end},even number=", get_even_number(begin, end))

date = [item for item in range(begin, end) if item % 2 == 0]
print(f"begin={begin},end={end},even number=", get_even_number(begin, end))