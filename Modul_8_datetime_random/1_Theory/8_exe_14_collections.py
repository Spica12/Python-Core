import collections

points = (0, 9, 8)
print(type(points), points)

print(points[2])

bank = (2234, 789, 176)
print(bank)

Bank = collections.namedtuple('Bank', ['cash', 'percent', 'NMT'])
bank_col = Bank(2234, 789, 176)
print(bank_col.cash, bank_col.percent, bank_col.NMT, sep='\t')