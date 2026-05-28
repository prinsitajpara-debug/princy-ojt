from collections import Counter

arr = [1, 2, 3, 2, 1, 4, 5, 5, 5]

count = Counter(arr)

duplicates = [num for num, freq in count.items() if freq > 1]

print(duplicates)