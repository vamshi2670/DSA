#normal stack 
# stack=[]

# stack.append(1)
# stack.append(2)
# stack.append(3)

# print(stack)
# #pop
# ele=stack.pop()
# print('element',ele)
# #peek
# peek=stack[-1]
# print('peek',peek)
# #length
# print('length:',len(stack))

#create stack using class

# class Stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,element):
#         self.stack.append(element)
#     def pop(self):
#         if self.isempty():
#             return 'stack is empty'
#         return self.stack.pop()
#     def isempty(self):
#         return len(self.stack)==0
#     def peek(self):
#         if self.isempty():
#             return 'stack is empty'
#         return self.stack[-1]
#     def length(self):
#         return len(self.stack)
# mystack=Stack()
# mystack.push(4)
# mystack.push(2)
# mystack.push(8)
# mystack.push(6)
# print("before operations:",mystack.stack)
# print('pop:',mystack.pop())
# print('peek:',mystack.peek())
# print('size:',mystack.length())
# print('isempty:',mystack.isempty())
# print('after:',mystack.stack)

#stack create using linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    
    def isEmpty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size

myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Pop: ", myStack.pop())
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())