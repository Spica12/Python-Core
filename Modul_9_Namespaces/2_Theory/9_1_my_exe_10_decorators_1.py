import webbrowser


def validator(func):
    def wrapper(url):          # wrapper - обгортка
        print('Some code before function')
        if '.' in url:
            func(url)
        else:
            print("Wrong url")
        print('Some code after function')

    return wrapper


@validator
def open_url(url):
    webbrowser.open(url)


open_url('https://itproger.com/ua')

