#Given a sequence of integers, find the second lowest integer
#sort array, print seq[1]

class SecLowest:
    def __init__(self, seq):
        self.seq = seq

    def sort(self):
        print(self.seq)
        self.seq.sort()
        return self.seq
    
    #find smallest, bring to start, cont until sorted
    def selection_sort(self):
        min = self.seq[0]
        new_seq = []

        for s in self.seq:
            if s < min:
                min = s

        new_seq.append(min)
        
        return new_seq

seq = [19,3,6,2,11,14,99,34]
seq2 = [33,4,5565,34,23,4536]
s = SecLowest(seq)

print(s.selection_sort())