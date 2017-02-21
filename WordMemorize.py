# Extract Word List
from random import shuffle
import Sequential
for i in range(17):
    Temp = open('Wordlist/words' + str(i) + '.txt', 'r')
    Temp2 = open('Meanlist/means' + str(i) + '.txt', 'r')
    locals()['A' + str(i)] = [line.strip() for line in Temp]
    locals()['B' + str(i)] = [line.strip() for line in Temp2]
# Choose Kind of Test
print "What kind do you want memorize? (random = r, sequential = s)"
kind = raw_input('>')
print "What kind do you want memorize? (word = w, mean = m)"
ki = raw_input('>')
print "And, what number do you want to Memorize? (1 - 17)"
num = raw_input('>')
print "Do you want to write erratas? (y or n)"
er = raw_input('>')
num = int(num)
A = locals()['A' + str(num - 1)]
B = locals()['B' + str(num - 1)]
if ki == 'w':
    ki = 0
elif ki == 'm':
    ki = 1
else:
    exit()


def Zipper(A, B):
    C = [[A[i], B[i]] for i in range(len(A))]
    return C


def Unzipper(C):
    A = [C[i][0] for i in range(len(C))]
    B = [C[i][1] for i in range(len(C))]
    return A, B


C = Zipper(A, B)
if kind == 'r':
    shuffle(C)
    A, B = Unzipper(C)
    T = Sequential.Memorize(num, A, B)
    if er == 'y':
        T.StartM(ki)
    elif er == 'n':
        T.StartN(ki)
elif kind == 's':
    A, B = Unzipper(C)
    T = Sequential.Memorize(num, A, B)
    if er == 'y':
        T.StartM(ki)
    elif er == 'n':
        T.StartN(ki)
