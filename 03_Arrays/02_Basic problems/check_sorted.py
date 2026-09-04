# Problem:Given an array, determine whether it is sorted in ascending order.
arr = [3,4,5,7,6]

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        print("Array is not sorted")
        break
else:
    print("Array is sorted")