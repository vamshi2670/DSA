#basic graph
vertex=['A','B','C','D']
adjecent_matrix=[
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,0],
    [1,1,1,0]
]
def print_matrix(matrix):
    for row in matrix:
        print(row)
print(vertex)
print_matrix(adjecent_matrix)

def connection(matrix,vertcess):
    for i in range (len(vertcess)):
        print(f"{vertcess[i]}:",end="")
        for j in range(len(vertcess)):
            if matrix[i][j]:
                print(vertcess[j],end=" ")
        print()
connection(adjecent_matrix,vertex)