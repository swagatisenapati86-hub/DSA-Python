# Find the frequency of a given number in an array.
def freq_of_given_no(arr,target):
    freq = 0 # for just one number we can use a counter variable to count the frequency of that number in the array.
    for i in arr:
        if i == target:
            freq += 1
    return freq

arr = [1, 2, 3, 2, 1, 4, 5, 3, 2]
target = 2
result = freq_of_given_no(arr,target)
print("Frequency of", target, "in the array is:",result)