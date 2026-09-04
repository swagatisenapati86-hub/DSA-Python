# Find largest element in an array.
arr = [1, 2, 3, 4, 5]
largest = arr[0]
for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print("Largest element in the array is:", largest)