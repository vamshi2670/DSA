
class Treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def preordertransversal(node):
    if node is None:
        return 
    print(node.data,end=',')
    preordertransversal(node.left)
    preordertransversal(node.right)
root=Treenode('R')
nodeA=Treenode('A')
nodeB=Treenode('B')
nodeC=Treenode('C')
nodeD=Treenode('D')
nodeE=Treenode('E')
nodeF=Treenode('F')
nodeG=Treenode('G')

root.left=nodeA
root.right=nodeB
nodeA.left=nodeC
nodeA.right=nodeD
nodeB.left=nodeE
nodeB.right=nodeF
nodeF.left=nodeG
preordertransversal(root)
print(root.left.right.data)