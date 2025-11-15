import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# graph=nx.Graph()
# graph.add_edges_from([('S','A'),('S','B'),('A','D'),('A','C'),('D','G'),('B','E'),('E','G')])
# nx.draw(graph,with_labels=True)
# plt.show()

Graph_dic={
    'S':['A','B'],
    'A':['C','D','S'],
    'B':['E','S'],
    'C':['A'],
    'D':['G','A'],
    'E':['B','G'],
    'G':['D','E']
}

def DFS(Graph,start,goal,Visited=None):
    path=[]
    if Visited is None:
        Visited=set()
    if start not in Visited:
        Visited.add(start)
        path.append(start)
        print(f"{start}->")
        if(start==goal):
            return path
        for i in Graph[start]:
            if i not in Visited:
                result=DFS(Graph,i,goal,Visited)
                if result:
                    return result
                

output=DFS(Graph_dic,"A","E")
print(output)
