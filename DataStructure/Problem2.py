# Queue ADT with Stack

#M1
class Queue():

    def __init__(self):
          self.enqueue_stack = []
          self.dequeue_stack = []

    def enqueue(self,data):
        self.enqueue_stack.append(data)

    def dequeue(self):
         
         if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
              raise Exception("Both Stacks are empty")
         
         if len(self.dequeue_stack) == 0:
              while len(self.enqueue_stack) != 0:
                   self.dequeue_stack.append(self.enqueue_stack.pop())
         
         return (self.dequeue_stack.pop())
    
queue = Queue()

queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(89)
queue.enqueue(101)

print(queue.dequeue())

queue.enqueue(23)

print(queue.dequeue())


#M2

class Q():
     
     def __init__(self):
          self.stack = []

     def enqueue(self,data):
          self.stack.append(data)

     def dequeue(self):
          
          if len(self.stack) == 1:
               return self.stack.pop()
          
          item = self.stack.pop()

          dequeud_item = self.dequeue()
           
          self.stack.append(item)

          return dequeud_item

queue = Q()

queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(89)
queue.enqueue(101)

print(queue.dequeue())

queue.enqueue(23)

print(queue.dequeue())



              
        




    



    
    

