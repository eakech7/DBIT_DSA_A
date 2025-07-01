def has_duplicates(list):
    for a in range(len(list)):
        for b in range(a + 1, len(list)):
            if list[a] == list[b]:
                return True
    return False

print(has_duplicates([10, 2, 4, 6, 10]))
print(has_duplicates([10, 9, 6, 7]))