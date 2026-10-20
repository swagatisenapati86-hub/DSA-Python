# Reverse printing
# Only displays elements in reverse order.	
# Original array remains unchanged.
arr = []
n = int(input("Enter the size of array:"))

print("Enter the elments:")
for i in range(n):
    arr.append(int(input()))

print("Array elments:",arr)

print("Array elements in reverse order:")
for i in range(n-1,-1,-1):
    print(arr[i], end=" ")
