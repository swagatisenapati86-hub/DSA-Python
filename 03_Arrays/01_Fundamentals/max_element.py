arr = [23,45,67,89]
maximum = arr[0]
for value in arr:
    if value > maximum:
        maximum = value
print("Maximum :", maximum)

# using shortcut
# arr = [23,45,67,89]
# maximum = max(arr)
# print("Maximum :", maximum)