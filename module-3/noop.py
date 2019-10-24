## using functools.wrap() to expose correct doc strings and help
import functools

def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    return noop_wrapper

@noop
def hello():
    """
        Prints a well known message.
        No input
    """
    print("Hello, World!")