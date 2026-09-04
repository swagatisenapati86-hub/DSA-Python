# Problem:Given an array and a target element, count how many times the target appears.
arr = [1,1,2,3,4,5,4,4,6,7,8]
target = int(input("Enter your target value to count:"))
count = 0

for i in range(len(arr)):
    if arr[i] == target:
        count += 1
        print("Target found at index:",i)

print("Target found a total of", count, "times.")