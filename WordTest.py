# Extract Word List
from random import shuffle
import Sequential
for i in range(17):
    Temp = open('words' + str(i) + '.txt', 'r')
    Temp2 = open('means' + str(i) + '.txt', 'r')
    locals()['A' + str(i)] = [line.strip() for line in Temp]
    locals()['B' + str(i)] = [line.strip() for line in Temp2]
# Choose Kind of Test
print "What kind do you want to Test? (Random = r, Sequential = s)"
kind = raw_input('>')
print "And, what number do you want to Test? (1 - 17)"
num = raw_input('>')
num = int(num)
A = locals()['A' + str(num - 1)]
B = locals()['B' + str(num - 1)]


def Zipper(A, B):
    C = [[A[i], B[i]] for i in range(len(A))]
    return C


def Unzipper(C):
    for i in range(len(C)):
        A[i] = C[i][0]
        B[i] = C[i][1]
    return A, B


if kind == 's':
    T = Sequential.Test(num, A, B)
    T.Start()
elif kind == 'r':
    C = Zipper(A, B)
    shuffle(C)
    A, B = Unzipper(C)
    T = Sequential.Test(num, A, B)
    T.Start()
else:
    print "Please input correct text."
    exit()
