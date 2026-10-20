# Reverse an array in place without using any extra space.
# You change the order of elements in the array itself.
# Swap elements to change the array.
arr = [1,2,3,4,5]
left = 0
right = len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Reversed array:", arr)