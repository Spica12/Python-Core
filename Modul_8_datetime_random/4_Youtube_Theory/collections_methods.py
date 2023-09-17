import collections


print('------------------------------------------------ .namedtuple()')

Movie = collections.namedtuple('Movie', ['title', 'year', 'director', 'genre'])

movie = Movie('Good Will Hunting', '1997', 'Gus Van Sant', 'Drama/Romance') 

print(movie)            # Movie(title='Good Will Hunting', year='1997', director='Gus Van Sant', genre='Drama/Romance')
print(movie.title)      # Good Will Hunting
print(movie.year)       # 1997
print(movie.director)   # Gus Van Sant
print(movie.genre)      # Drama/Romance

print(movie[0])         # Good Will Hunting
print(movie[1])         # 1997
print(movie[2])         # Gus Van Sant
print(movie[3])         # Drama/Romance

try:
    movie[1] = 2008
except TypeError:
    print('TypeError: You can\'t change!')

print('------------------------------------------------ .namedtuple()')
text = """One of Guido’s key insights is that code is read much more often than it is written. The guidelines provided here are intended to improve the readability of code and make it consistent across the wide spectrum of Python code. As PEP 20 says, “Readability counts”.

A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.

However, know when to be inconsistent – sometimes style guide recommendations just aren’t applicable. When in doubt, use your best judgment. Look at other examples and decide what looks best. And don’t hesitate to ask!

In particular: do not break backwards compatibility just to comply with this PEP!"""

print(text.count('style'))

words = text.split()
print(words)

result = collections.Counter(words)
print(result)

for word, counter in result.items():
    print(f'{word} - {counter}')

print('------------------------------------------------ .most_common()')

most_common_values = result.most_common(3)
print(most_common_values)       # [('is', 7), ('to', 4), ('of', 3)]

print('------------------------------------------------ .defaultdict()')
a = {'a': 1}

try:
    print(a['b'])
except KeyError:
    print('KeyError: This object doesn\'t create')

print('------------------------------------------------ .deque()')
my_deque = collections.deque()
print(my_deque)         # deque([])

my_deque.append('1')
print(my_deque)         # deque(['1'])

my_deque.appendleft('0')
print(my_deque)         # deque(['0', '1'])

value = my_deque.popleft()
print(value, my_deque)  # 0 deque(['1'])

my_deque.insert(0, ['2'])
print(my_deque)  # deque([['2'], '1'])





