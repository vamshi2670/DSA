
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
node1=Node(3)
node2=Node(2)
node3=Node(8)
node4=Node(6)

node1.next=node2
node2.prev=node1
node2.next=node3
node3.prev=node2
node3.next=node4
node4.prev=node3

currentnode=node1
while currentnode:
    print(currentnode.data,end='->')
    currentnode=currentnode.next
print('null')

currentnode=node4
while currentnode:
    print(currentnode.data,end='->')
    currentnode=currentnode.prev
print('null')