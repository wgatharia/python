class Trace:
    def __init__(self):
        self.enabed = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabed:
                print("Calling %s" % f)
            return f(*args, **kwargs)
        return wrap

#create an instance of trace and use it as a function decorator

tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

#test

l = [1, 2, 3, 4]

print(l)
l = rotate_list(l)
print(l)

l = rotate_list(l)
print(l)