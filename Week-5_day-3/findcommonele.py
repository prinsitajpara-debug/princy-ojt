#find the most common element in a list
from collections import Counter

list=[1,2,4,3,5,1,3,2,3,3,6,2,2,8,9,4,8,9]

counter=Counter(list)

common_elements=counter.most_common(1)[0][0]

print(common_elements)
