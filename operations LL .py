#transverse means from one node to next node

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def transvers(head):
#         currnetnode=head
#         while currnetnode:
#             print(currnetnode.data,end='->')
#             currnetnode=currnetnode.next
#         print('null')
# node1=Node(2)
# node2=Node(1)
# node3=Node(6)
# node4=Node(5)

# node1.next=node2
# node2.next=node3
# node3.next=node4

# transvers(node1)


# finding lowest value 
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def Lowestval(head):
#     minival=head.data
#     currentnode=head.next
#     while currentnode:
#         if currentnode.data<minival:
#            minival=currentnode.data
#         currentnode=currentnode.next
#     return minival
# node1=Node(2)
# node2=Node(3)
# node3=Node(1)
# node4=Node(5)

# node1.next=node2
# node2.next=node3
# node3.next=node4

# print(Lowestval(node1))

#delete specified node

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def transverse(head):
#     currentnode=head
#     while currentnode:
#         print(currentnode.data,end='->')
#         currentnode=currentnode.next
#     print('null')

# def nodedelete(head,delnode):
#     if head==delnode:
#         return head.next
#     currentnode=head
#     while currentnode.next and currentnode.next!= delnode:
#         currentnode=currentnode.next
#     if currentnode.next is None:
#         return head
#     currentnode.next=currentnode.next.next
#     return head
# node1=Node(2)
# node2=Node(3)
# node3=Node(1)
# node4=Node(5)

# node1.next=node2
# node2.next=node3
# node3.next=node4        

# node1=nodedelete(node1,node3)
# transverse(node1)

#insertion node

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def transverse(head):
    currentnode=head
    while currentnode:
        print(currentnode.data,end='->')
        currentnode=currentnode.next
    print('null')
def insertnode(head,newnode,position):
    if position==1:
        newnode.next=head
        return newnode
    currentnode=head
    for _ in range(position - 2):
        if currentnode is None:
            break
        currentnode =currentnode.next
    newnode.next=currentnode.next
    currentnode.next=newnode
    return head

node1=Node(2)
node2=Node(3)
node3=Node(1)
node4=Node(5)

node1.next=node2
node2.next=node3
node3.next=node4        
Newnode=Node(9)
n1=insertnode(node1,Newnode,2)
transverse(n1)