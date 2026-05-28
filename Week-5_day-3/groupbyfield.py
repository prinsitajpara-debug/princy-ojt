# import pandas as pd

# data = {
#     "name": ["A", "B", "A", "C", "B"],
#     "marks": [80, 90, 70, 60, 85]
# }

# df = pd.DataFrame(data)

# result = df.groupby("name")["marks"].sum()

# print(result)


data = [
    ("A", 80),
    ("B", 90),
    ("A", 70),
    ("C", 60),
    ("B", 85)
]
from collections import defaultdict

group = defaultdict(list)

[group[name].append(marks) for name, marks in data]

print(dict(group))