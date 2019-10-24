###uses a function decorator
## a decorator is implemented as callable that take and return other callables

def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        print(x)
        return ascii(x)
    return wrap #new callable object

@escape_unicode
def copy_right():
    return '© William Gatharia 2019'

print(copy_right())