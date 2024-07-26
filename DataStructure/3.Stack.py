class Stack:
    def __init__(self):
        self.stack = []

    #Insert item into stack O(1) 
    def push(self,data):
        self.stack.append(data)

    #Remove and return the last item we have insertd O(1) 
    def pop(self):

        if self.stack_size() < 1:
            return -1
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    #Peek: It returns the last item without removing it O(1)
    def peek(self):
        return self.stack[-1]

    #O(1)
    def is_empty():
        return self.stack == []
    
    def stack_size(self):
        return len(self.stack)
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print('Size: %d' % stack.stack_size())
print('Popped item: %d' % stack.pop())
print('Size: %d' % stack.stack_size())
print('Peek item: %d' % stack.peek())
print('Size: %d' % stack.stack_size())
print('Popped item: %d' % stack.pop())
print('Popped item: %d' % stack.pop())
print('Popped item: %d' % stack.pop())
print('Popped item: %d' % stack.pop())

