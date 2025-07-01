def find_min(list):
    min_value = list[0]
    for num in list[1:]:
        if num < min_value:
            min_value = num
    return min_value

print(find_min([10,12,55,7]))
