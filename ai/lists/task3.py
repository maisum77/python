import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import collections

Graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':['G'],
    'E':['G'],
    'F':['G']
}
# diagram=nx.Graph()
# diagram.add_edges_from([('A','B'),('A','C'),('B','D'),('B','E'),('A','B'),('C','F'),('A','B'),('D','G'),('E','G'),('F','G')])
# nx.draw(diagram,with_labels=True)
# plt.show()

def BFS(graph,start,goal):
    path=[]
    visited={start}
    Queue=deque([start])
    while Queue:
        node=Queue.popleft()
        path.append(node)
        print(node,end=" ")
        if(node==goal):
            return path
        for i in graph[node]:
            if i not in visited:
                Queue.append(i)
                visited.add(i)

output=BFS(Graph,"A","G")
print(output)