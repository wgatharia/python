## a function that returns a new specialized function
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


##test
square = raise_to(2)
print(square.__closure__)
print("square(5)=", square(5))

print("square(9)=", square(9))

print("square(1234)=", square(1234))

cube = raise_to(3)
print(cube.__closure__)

print("cube(3)=", cube(3))