sequence = [2,9,82,32,56,78,3,22,22,24,65,11]

def quicksort(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq.pop()
        less = []
        more = []

        for s in seq:
            if s < pivot:
                less.append(s)
            else:
                more.append(s)
        return quicksort(less) + [pivot] + quicksort(more)

print(quicksort(sequence))