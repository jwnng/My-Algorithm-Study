from collections import Counter
numbers = [1, 3, 4, 1, 2, 2, 3, 2, 2]
counter = {}

counter = Counter(numbers)
print(counter)
print(counter.keys())
print(counter.values())
print(counter.items())

print(counter.most_common()[0][0])