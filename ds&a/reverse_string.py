import stack

string = "puddaw"
reversed_string = ""
s = stack.Stack()

for l in string:
    s.push(l)

while not s.isempty():
    reversed_string += s.pop()

print(reversed_string)