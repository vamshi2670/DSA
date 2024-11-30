# queue=[]
# queue.append(2)
# queue.append(4)
# queue.append(5)
# queue.append(8)
# #dequeue
# dequeue=queue.pop(0)
# print('dequeue:',dequeue)
# #peek
# peek=queue[0]
# print('peek:',peek)
# #isempty
# print('isempty:',len(queue)==0)
# #size
# print('size:',len(queue))

class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if self.isempty():
            return 'queue is empty'
        return self.queue.pop(0)
    def peek(self):
        if self.isempty():
            return 'queue is empty'
        return self.queue[0]
    def isempty(self):
        return len(self.queue)==0
    def size(self):
        return len(self.queue)
myqueue=Queue()
myqueue.enqueue('a')
myqueue.enqueue('b')
myqueue.enqueue('c')
myqueue.enqueue('d')

print('before :',myqueue.queue)
print('dequeue:',myqueue.dequeue())
print('peek:',myqueue.peek())
print('isempty:',myqueue.isempty())
print('size:',myqueue.size())

#create queue using liked list 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", end="")
myQueue.printQueue()

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())