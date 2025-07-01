def linear_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

print("Index:", linear_search([5, 3, 7, 1], 7))        
print("Index:", linear_search([5, 3, 7, 1], 4)) 