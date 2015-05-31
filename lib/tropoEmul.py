#
# Library name: tropoEmul 
#
# This is a non-complete library to emulate the functionality of the 
# Python API of tropo. See https://www.tropo.com/docs/scripting for
# further details.

import sys

class resultType:
    def __init__(self):
        self.value = None

result = resultType()

def answer(timeout=None):
    if timeout is not None:
        wait(timeout)

    print 'Answering call.'


def ask(text, args=None):
    print 'Asking question ' + repr(text) + '.'

    if args is not None:
        txt = sys.stdin.readline()
        txt = txt[:-1]
        result.value = txt
        if args['onChoice'] is not None:
            args['onChoice'](1)

def call(destination, args=None):
    pass

def conference(number):
    pass

def getHeader():
    pass

def hangup():
    pass

def log():
    pass

def message(string):
    pass

def record():
    pass

def redirect():
    pass

def reject():
    pass

def say(string):
    print 'Saying ' + repr(string) + '.'

def startCallRecording():
    pass

def stopCallRecording():
    pass

def transfer(number):
    pass

def wait(timeout):
    print 'Waiting for ' + str(timeout) + ' seconds.'


