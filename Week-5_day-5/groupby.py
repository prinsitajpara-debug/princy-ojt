from itertools import groupby
data=sorted([1,2,3,3,2,1,4,5])
for key,group in groupby(data):
    print(key,list(group))