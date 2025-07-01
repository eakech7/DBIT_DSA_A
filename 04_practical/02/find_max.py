def find_max(list):
    max_value = list[0]
    for num in list[1:]:
        if num > max_value:
            max_value = num
    return max_value

print(find_max([10, 2, 6, 8, 25]))