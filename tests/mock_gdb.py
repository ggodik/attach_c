class Command(object):
    def __init__(self,*args):
        pass


    def invoke (self, arg, from_tty):
         print "Hello, World!"

COMMAND_NONE = 'FAKE-COMMAND'
