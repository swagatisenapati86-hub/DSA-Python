# Copy an array to another array.
arr = [1, 2, 3, 4, 5]
new_arr = []
for i in range(len(arr)):
    new_arr.append(arr[i])

print("Original array:", arr)
print("Copied array:", new_arr)