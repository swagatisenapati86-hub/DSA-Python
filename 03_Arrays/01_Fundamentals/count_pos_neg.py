arr = []
n = int(input("Enter the size of array:"))

print("Enter the array elements:")
for i in range(n):
    arr.append(int(input()))

print("Array elements:",arr)

pos = 0
neg = 0

for i in arr:
    if i < 0:
        neg  += 1
    else:
        pos += 1
print("No. of positive integers:",pos)
print("No. of negative integers:",neg)