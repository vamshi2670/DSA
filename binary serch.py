# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def search(node, target):
#     if node is None:
#         return None 
#     elif node.data == target:
#         return node
#     elif target < node.data:
#         return search(node.left, target)
#     else:
#         return search(node.right, target)

# root = TreeNode(13)
# node7 = TreeNode(7)
# node15 = TreeNode(15)
# node3 = TreeNode(3)
# node8 = TreeNode(8)
# node14 = TreeNode(14)
# node19 = TreeNode(19)
# node18 = TreeNode(18)

# root.left = node7
# root.right = node15
# node7.left = node3
# node7.right = node8
# node15.left = node14
# node15.right = node19
# node19.left = node18
# # Search for a value
# result = search(root, 3)
# if result:
#     print(f"Found the node with value: {result.data}")
# else:
#     print("Value not found in the BST.")

#Compare each node:
#Is the value lower? Go left.
#Is the value higher? Go right.

#insert a value
class Treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(node,data):
    if node is None:
        return Treenode(data)
    else:
        if data<node.data:
            return insert(node.left,data)
        elif data>node.data:
            return insert(node.right,data)
    return node
def inordertransverse(node):
    if node is None:
        return
    print(inordertransverse(node.left))
    print(node.data,end=',')
    print(inordertransverse(node.right))
root=Treenode(10)
node5=Treenode(5)
node20=Treenode(20)
node3=Treenode(3)
node8=Treenode(8)
node15=Treenode(15)
node25=Treenode(25)
node21=Treenode(21)

root.left=node5
root.right=node20
node5.left=node3
node5.right=node8
node20.left=node15
node20.right=node25
node25.left=node21

print(insert(root,10))
inordertransverse(root)

#lowest value
class Treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inordertranseversal(node):
    inordertranseversal(node.left)
    print(node.data,end=',')
    inordertranseversal(node.right)
def lowest(node):
    current=node
    while current.left is not None:
        current=node.left
    return current
root=Treenode(10)
node5=Treenode(5)
node20=Treenode(20)
node3=Treenode(3)
node8=Treenode(8)
node15=Treenode(15)
node25=Treenode(25)
node21=Treenode(21)

root.left=node5
root.right=node20
node5.left=node3
node5.right=node8
node20.left=node15
node20.right=node25
node25.left=node21

print('lowest value',lowest(root).data)
inordertranseversal(root)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node, data):
    if not node:
        return None

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        # Node with only one child or no child
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp

        # Node with two children, get the in-order successor
        node.data = minValueNode(node.right).data
        node.right = delete(node.right, node.data)

    return node

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# Traverse
inOrderTraversal(root)

# Delete node 15
delete(root,15)

# Traverse
print() # Creates a new line
inOrderTraversal(root)