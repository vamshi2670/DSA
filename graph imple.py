#graph implementaion
class Graph:
    def __init__(self,size):
        self.add_matrix=[[0]*size for _ in range(size)]
        self.size=size
        self.vertex_data=[' ']* size
def add_adges(self,u,v):
    if 0<=u<self.size and 0<=v<self.size:
        self.add_matrix[u][v]=1
        self.add_matrix[v][u]=1
def add_vertex(self,vertex,data):
    if 0<=vertex<self.size:
        self.vertex_data[vertex]=data
def graph(self):
    for row in self.add_matrix:
        print(''.join(map(str,row)))   #syntax:map(function,iterable)ex:
                                                    #def squre(x):
                                                        #return x*x
                                                        #arr=[3,5,7,8,2]
                                                        #squre_nums=list(map(squre,arr))
                                                        #print(squre_nums)
        for vertex ,data in enumerate (self.vertex_data):
            print(f"{vertex}:{data}")
g=Graph()
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1)  # A - B
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(1, 2)  # B - C

g.print_graph()