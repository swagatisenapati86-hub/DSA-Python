arr = [2,3,45,78,87,98]
minimum = arr[0]
for value in arr:
    if value < minimum:
        minimum = value
print("Minimum:", minimum)

# using shortcut
# arr = [2,3,45,78,87,98]
# minimum = min(arr)
# print("Minimum:", minimum)
