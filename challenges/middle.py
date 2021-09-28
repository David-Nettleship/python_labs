#https://pythonprinciples.com/challenges/Middle-letter/

def mid(s):
    if(len(s) % 2 != 0):
        mid = len(s)/2
        print(mid)
        s = (s[mid])
    else:
        return ""
    return s

print(mid("abc"))
print(mid("abcd"))
print(mid("abcde"))