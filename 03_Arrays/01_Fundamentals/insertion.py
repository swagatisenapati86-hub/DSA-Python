#insertion in array
arr = []
n = int(input("Enter the size of array:"))

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

print("Array elements are:",arr)

ele = int(input("Enter the element to insert:"))
pos = int(input("Enter the pos:"))

if pos < 1 and pos > n+1:
    print("Invalid position")

else:
    arr.insert(pos-1,ele)
    print("Array after insertion:",arr)