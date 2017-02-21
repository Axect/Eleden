class Test(object):
    def __init__(self, num, A, B):
        self.A = A
        self.B = B
        self.num = num

    def Main_eng(self):
        Er = open("Erratas/Errata_word" + str(self.num) + ".txt", 'w')
        for i in range(len(self.A)):
            print str(i) + '. %s' % self.A[i]
            print "Do you know this word? If you know press y, else press n"
            self.know = raw_input('>')
            if self.know == 'y':
                print str(i) + '. %s' % self.B[i]
                print "Correct = y, Incorrect = n"
                cor = raw_input('>')
                if cor == 'n':
                    Er.write(self.A[i] + '\n')
                    print "Save Complete!"
                elif cor == 'y':
                    pass
                else:
                    print "Please input correct text"
                    break
            elif self.know == 'n':
                Er.write(self.A[i] + '\n')
                print "Save Complete!"
            else:
                print "Please input correct text"
                break
            Er.close()

    def Main_kor(self):
        Er = open("Erratas/Errata_mean" + str(self.num) + ".txt", 'w')
        for i in range(len(self.A)):
            print str(i) + '. %s' % self.B[i]
            print "Do you know this word? If you know press y, else press n"
            self.know = raw_input('>')
            if self.know == 'y':
                print str(i) + '. %s' % self.A[i]
                print "Correct = y, Incorrect = n"
                cor = raw_input('>')
                if cor == 'n':
                    Er.write(self.B[i] + '\n')
                    print "Save Complete!"
                elif cor == 'y':
                    pass
                else:
                    print "Please input correct text"
                    break
            elif self.know == 'n':
                Er.write(self.B[i] + '\n')
                print "Save Complete!"
            else:
                print "Please input correct text"
                break
            Er.close()

    def Start(self):
        print "What kind do you want to test? (word = w, mean = m)"
        kind = raw_input('>')
        if kind == 'w':
            self.Main_eng()
        elif kind == 'm':
            self.Main_kor()
        else:
            print "Put correct text"


class Memorize(object):
    def __init__(self, num, A, B):
        self.num = num
        self.A = A
        self.B = B

    def StartM(self, num):
        Er = open("Erratas/Errata" + str(self.num), 'w')
        if num == 0:
            for i in range(len(self.A)):
                print self.A[i]
                t = raw_input('>')
                if t == 's':
                    Er.write(self.A[i] + '\n')
                print self.B[i]
            Er.close()
        elif num == 1:
            for i in range(len(self.A)):
                print self.B[i]
                t = raw_input('>')
                if t == 's':
                    Er.write(self.B[i] + '\n')
                print self.A[i]
            Er.close()

    def StartN(self, num):
        if num == 0:
            for i in range(len(self.A)):
                print self.A[i]
                raw_input('>')
                print self.B[i]
        elif num == 1:
            for i in range(len(self.A)):
                print self.B[i]
                raw_input('>')
                print self.A[i]
