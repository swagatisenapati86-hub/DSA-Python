# Second largest element in an array.

# Brute force approach: Sort the array and return the second last element.
def second_largest(arr):
    arr.sort()
    return arr[-2]

arr = [34,65,23,45,76,12]
print("Second largest element in the array is:", second_largest(arr))

# Better approach: two pass approach
def second_largest(arr):
    largest = sec_largest = float('-inf')
    for i in arr:
        largest =max(largest,i)
    for i in arr:
        if i != largest and i > sec_largest:
            sec_largest = i
    return sec_largest  

arr = [34,65,23,45,76,12]
print("Second largest is:", second_largest(arr))  
        


# Optimal approach: single pass approach
def second_largest(arr):
    largest = second_largest = float('-inf')
    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i
    return second_largest

arr = [34,65,23,45,76,12]
print("Second largest is:", second_largest(arr))
