from functools import reduce

print(help(reduce))

"""
Help on built-in function reduce in module _functools:
reduce(...)
    reduce(function, iterable[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence
    or iterable, from left to right, so as to reduce the iterable to a single
    value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the iterable in the calculation, and serves as a default when the
    iterable is empty.

None
PS D:\GoIT\Python Core\Modul_9_Namespaces> & C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe "d:/GoIT/Python Core/Modul_9_Namespaces/5_Youtube_practice/9_2_you_exe_6_filter.py"
Help on class filter in module builtins:

class filter(object)
 |  filter(function or None, iterable) --> filter object
 |
 |  Return an iterator yielding those items of iterable for which function(item)
 |  is true. If function is None, return the items that are true.
 |
 |  Methods defined here:
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __next__(self, /)
 |      Implement next(self).
 |
 |  __reduce__(...)
 |      Return state information for pickling.
 |
 |  ----------------------------------------------------------------------
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
"""

x = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(x)       # ((((1 + 2) + 3) + 4) + 5) = 15