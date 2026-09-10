# Count frequency of each element
def count_freq(arr):
    freq = {}
    for x in arr:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
        # freq[x] = freq.get(x,0) + 1 (or can use this get method instead of if else)
    return freq

arr = [1, 2, 3, 2, 1, 4, 5, 3, 2]
result = count_freq(arr)
print("Frequency of each element in the array is:", result)
