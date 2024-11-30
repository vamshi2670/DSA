class Treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Treenode('r')
nodea=Treenode('a')
nodeb=Treenode('b')
nodec=Treenode('c')
noded=Treenode('d')
nodee=Treenode('e')
nodef=Treenode('f')
nodeg=Treenode('g')

root.left=nodea
root.right=nodeb
nodea.left=nodec
nodea.right=noded
nodeb.left=nodee
nodeb.right=nodef
nodee.left=nodeg

def inordertransversal(node):
    if node is None:
        return
    inordertransversal(node.left)
    print(node.data ,end=',')
    inordertransversal(node.right)
inordertransversal(root)