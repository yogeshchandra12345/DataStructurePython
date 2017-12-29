import sys
import time
class vertex:
    def __init__(self,node):
        self.id=node
        self.adjacent={}
        self.visited=False
        self.previous=None
        self.distance=sys.maxsize
    def __lt__(self, other):
        if isinstance(other,self.__class__):
            return self.distance < other.distance


class graph:
    def __init__(self):
        self.v={}
        self.nv=0

    def __iter__(self):
        return iter(self.v.values())
    def add_vertex(self,node):
        newvertex=vertex(node)
        self.v[node]=newvertex
        return newvertex
    def add_edge(self,frm,to,cost):
        if frm not in self.v:
            self.add_vertex(frm)
        if to not in self.v:
            self.add_vertex(to)

        fv=self.v[frm]
        tv=self.v[to]
        fv.adjacent[tv]=cost
        tv.adjacent[fv]=cost
    def getedge(self):
        edge=[]
        for v in self.v.values():
            for e in v.adjacent.keys():
                edge.append((v.id,e.id,v.adjacent[e]))
        for i in edge:
            print(i)
import heapq
def dijkstra(g,start):
    start_vertex=g.v[start]
    start_vertex.distance=0
    l = [(i.distance, i) for i in g.v.values()]
    heapq.heapify(l)
    while len(l):
        current=heapq.heappop(l)[1]
        current.visited=True
        for next in current.adjacent.keys():
            if next.visited:
               continue
            newd=current.distance+current.adjacent[next]
            if newd<next.distance:
                next.distance=newd
                next.previous=current
            else:
                pass
        heapq.heapify(l)

def shortest(v, path):
    if v.previous:
        path.append(v.previous.id)
        shortest(v.previous, path)
    return

g=graph()
g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_vertex('f')

g.add_edge('a', 'b', 7)
g.add_edge('a', 'c', 9)
g.add_edge('a', 'f', 14)
g.add_edge('b', 'c', 10)
g.add_edge('b', 'd', 15)
g.add_edge('c', 'd', 11)
g.add_edge('c', 'f', 2)
g.add_edge('d', 'e', 6)
g.add_edge('e', 'f', 9)
t=time.clock()
print (time.clock())
dijkstra(g,'a')
print (time.clock()-t)
print (time.clock())
for t in ['d','e','f']:
    path=[t]
    V=g.v[t]
    shortest(V,path)
    print ('The shortest path : %s' %(path[::-1]))
print (time.clock())
