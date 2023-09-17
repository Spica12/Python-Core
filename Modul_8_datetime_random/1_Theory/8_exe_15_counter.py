import collections

temps = [0.5, 0.0, -3.5, 0.0, 2.0, -3.5]

temps_count = collections.Counter(temps)
print(temps_count)
print(temps_count.most_common(2))