# Find smallest element in an array.
arr = [1, 2, 3, 4, 5]
smallest = arr[0]
for i in range(1,len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]

print("Smallest element in the array is:", smallest)