class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(3)
node2=Node(4)
node3=Node(9)
node4=Node(2)
node5=Node(5)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

currentnode=node1
while currentnode:
    print(currentnode.data,end='->')
    currentnode=currentnode.next
print('null')