import sys
class vertex:
    def __init__(self,data):
        self.value=data
        self.distance=0
        self.visited=False
        self.adjacent={}
        self.previous=None


class graph:
    def __init__(self,n):
        self.vertices={}
        self.nofvertices=n

    def add_vertex(self,data):
        nv=vertex(data)
        self.vertices[data]=nv

    def add_edge(self,frm,to,cost):
        if not self.vertices[frm]:
            self.add_vertex(frm)
        if not self.vertices[to]:
            self.add_vertex(to)
        fv=self.vertices[frm]
        tv=self.vertices[to]
        self.vertices[frm].adjacent[tv]=cost
        self.vertices[to].adjacent[fv]=cost

def find(parent,i):
    if parent[i]==i:
        return i
    else:
        parent[i]=find(parent,parent[i])
        return parent[i]

def union(parent,rank,x,y):
    xp=find(parent,x)
    yp=find(parent,y)
    if rank[xp]>rank[yp]:
      parent[yp]=xp
    elif rank[yp]>rank[xp]:
        parent[xp]=yp
    else:
        parent[yp]=xp
        rank[xp]+=1


def iscycle(g,parent,rank):
    for i in g.vertices.values():
        for j in i.adjacent:
            if j.previous != i and i.previous != j:
                j.previous = i
                i.previous = j
                if find(parent,i.value)==find(parent,j.value):
                    return True
                else:
                  union(parent,rank,i.value,j.value)
    return False


if __name__=='__main__':
    parent =[]
    rank=[]
    nofvertices=6
    for i in range(nofvertices):
        parent.append(i)
        rank.append(0)
    g=graph(6)
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_edge(0,1,9)
    g.add_edge(1,2,6)
    g.add_edge(2,3,7)
    g.add_edge(3,4,8)
    g.add_edge(4,5,9)
    for i in g.vertices.values():
        print (i.value,i.distance,end=':> ')
        for next in i.adjacent:
            print(next.value,i.adjacent[next],end=',')
        print()

    print (iscycle(g,parent,rank))


