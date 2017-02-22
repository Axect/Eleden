from time import sleep
from subprocess import call
print "Welcome to Word Knights"
sleep(1)
print "Select work type:"
work = raw_input('New or Open: >')
print "Filename? (_word.txt or _mean.txt are auto attched)"
name = raw_input('>')


def Save(name, W, M):
    Text = open('Extra/' + name + '_word.txt', 'r')
    Text2 = open('Extra/' + name + '_mean.txt', 'r')
    Temp = [line.strip() for line in Text]
    Temp2 = [line.strip() for line in Text2]
    for i in range(len(W)):
        Temp.append(W[i])
        Temp2.append(M[i])
    Text.close()
    Text2.close()
    Text = open('Extra/' + name + '_word.txt', 'w')
    Text2 = open('Extra/' + name + '_mean.txt', 'w')
    for i in range(len(Temp)):
        Text.write(Temp[i] + '\n')
        Text2.write(Temp2[i] + '\n')
    Text.close()
    Text2.close()


if work == 'New':
    command = 'touch Extra/' + name + '_word.txt Extra/' + name + '_mean.txt'
    call(command, shell=True)
elif work == 'Old':
    pass
W = []
M = []
while True:
    print "Word:"
    word = raw_input('>')
    print " Mean:"
    mean = raw_input('>')
    W.append(word)
    M.append(mean)
    print "Stop or Continue? (Stop = s, Continue = c)"
    stop = raw_input('>')
    if stop == 's':
        Save(name, W, M)
        break
    elif stop == 'c':
        continue

