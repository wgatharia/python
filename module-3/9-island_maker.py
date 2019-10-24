##using multiple decorators

def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

class Trace:
    def __init__(self):
        self.enabed = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabed:
                print("Calling %s" % f)
            return f(*args, **kwargs)
        return wrap

tracer = Trace()


@tracer
@escape_unicode
def my_island_maker(name):
    return name + '∞'

##decorating in a class method

class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    @escape_unicode
    def my_island_maker(self, name):
        return name + self.suffix


##test. Lets make some infinite island names

print(my_island_maker('Hulu'))

print(my_island_maker('Gamma'))

tracer.enabed = False

print(my_island_maker('Kilo'))

#test using class

im = IslandMaker(' Island')

print(im.my_island_maker('King'))

im = IslandMaker(' ∊')

print(im.my_island_maker('British'))