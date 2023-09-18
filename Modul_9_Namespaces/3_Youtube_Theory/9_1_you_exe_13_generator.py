


def func():
    print('Entry point')

    yield None
    print('After yield')



#  Variant 1 - Don't work -----------------------
func()          # Nothing !!!



#  Variant 2 - Don't work -----------------------
next(func())    # Entry point
next(func())    # Entry point



#  Variant 3 - It's work! -----------------------
generator = func()
next(generator) # Entry point
next(generator) # After yield