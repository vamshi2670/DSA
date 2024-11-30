
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(3)
node2=Node(2)
node3=Node(8)
node4=Node(6)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node1

currentnode=node1
startnode=node1

print(currentnode.data,end='->')
currentnode=currentnode.next

while currentnode!=startnode:
    print(currentnode.data,end='->')
    currentnode=currentnode.next
print('...')