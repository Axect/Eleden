from time import sleep
from subprocess import call
print "Welcome to Word Knights"
sleep(1)
print "Select work type:"
type = raw_input('New or Open: >')
if type == 'New':
    while True:
print "Word:"
word = raw_input('>')
print ""
