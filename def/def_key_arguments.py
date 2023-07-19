print('----------- Example 1 ----------')

def func(a, b=5, c=10):
    print('a equal', a, ', b equal', b, ', c equal', c)

func(3, 7)          # | a=3   | b=7 | c=10 |
func(25, c=24)      # | a=25  | b=5 | c=24 |
func(c=50, a=100)   # | a=100 | b=5 | c=50 |

print('----------- Example 2 ----------')

def say(message, times=1):
    print(message * times)

say('Hello World!') # Hello World!
say('Hello', 5)     # HelloHelloHelloHelloHello
