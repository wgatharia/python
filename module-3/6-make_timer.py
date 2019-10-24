#introduce names from enclosing namespace into the local namespace
#use nonlocal keyword

import time

def make_timer():
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()

        if last_called is None:
            last_called = now
            return None
        
        result = now - last_called
        last_called = now
        return result
    return elapsed

#test
#returns time last first invocation
t = make_timer()

print(t())

time.sleep(2)

print(t())

time.sleep(3)

print(t())

time.sleep(4)

print(t())
