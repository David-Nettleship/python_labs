#Given a sequence of integers, find the second lowest integer
#sort array, print seq[1]

class SecLowest:
    def __init__(self, seq):
        self.seq = seq

    def sort(self):
        print(self.seq)
        self.seq.sort()
        return self.seq

seq = [19,3,6,2,11,14,99,34]
seq2 = [33,4,5565,34,23,4536]
s = SecLowest(seq)
s2 = SecLowest(seq2)
print(s.sort())
print(s2.sort())