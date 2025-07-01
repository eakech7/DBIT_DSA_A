<<<<<<< HEAD
def linear_search(values):
    target = int(input("Enter values to serach: "))
    for index, item in enumerate (values):
        print(f"Current value is {item}")
        if item == target:
            return index
        
    return -1
    
values = [-1,9,8,7,6,5,4,3,-2,1]
print(f"List of values {values}")

ans = linear_search(values)

if ans != -1:
    print(f"{values[ans]} found at index {ans}")
else:
    print("not found")
    
print(ans)
=======
 
>>>>>>> 6a74da2c137cd10f45c06333a2b1522f11cae891
