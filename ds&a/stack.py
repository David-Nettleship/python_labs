class Stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    s1 = Stack()
    s1.push(5)
    s1.push(7)
    print(s1.peek())
    s1.pop()
    print(s1.peek())
    print(s1.size())