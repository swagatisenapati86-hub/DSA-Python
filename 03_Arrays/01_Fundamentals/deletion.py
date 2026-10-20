#deletion in array
arr = []
n = int(input("Enter the size of array:"))

print("Enter the array elements:")
for i in range(n):
    arr.append(int(input()))

print("Array elements:",arr)

pos = int(input("Enter the position to delete:"))

if pos < 1 and pos > n+1:
    print("Invalid element")
else:
    arr.pop(pos-1)
    print("Array after deletion:",arr)