#gloal message
message = 'global'

def enclosing():
    message = 'enclosing'

    def local():
        #use global keyword to change message
        global message
        message = 'local'

    print('enclosing message: ', message)
    local()
    print('enclosing message: ', message)

print('global message: ', message)
enclosing()
print('enclosing message: ', message)