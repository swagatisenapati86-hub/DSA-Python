#Problem: Given an array and a target, determine whether the target exists in the array.
arr = [4,5,6,78,9,20]
target=int(input("Enter the target value to search:"))

found = False

for i in range(len(arr)):
    if arr[i] == target:
        found = True
        print("Target found at index:",i)
        break

if not found:
    print("Target not found")

#using for-else loop
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("Target found at index", i)
#         break
# else:
#     print("Target not found")