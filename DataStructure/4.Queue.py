class Queue():

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []
    
    # O(1)
    def enqueue(self,data):
        self.queue.append(data)

    # O(N). How to Solve this problem? Use Linked list, infact doubly linked list, so that enqueue remains O(1)
    def dequeue(self):
        if self.size_queue() != 0: 
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return -1
    
    def peek(self):
        return self.queue[0]
    
    def size_queue(self):
        return len(self.queue)
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print('Size: %d' % queue.size_queue())
print('Dequeue: %d' % queue.dequeue())
print('Size: %d' % queue.size_queue())
print('Dequeue: %d' % queue.dequeue())
print('Dequeue: %d' % queue.dequeue())
print('Dequeue: %d' % queue.dequeue())
print('Dequeue: %d' % queue.dequeue())
print('Dequeue: %d' % queue.dequeue())
