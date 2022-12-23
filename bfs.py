from collections import deque 
from math import inf
class Node:
    def __init__(self,ID,state=None,g=inf,h=None,c=None,p=None):
        self.ID=ID
        self.state=state
        self.g=g
        self.h=h
        self.c=c
        self.p=p
class Problem:
    def __init__(self,graph,initial_state,goal_state):
        self.graph=graph
        self.initial_state=initial_state
        self.goal_state=goal_state
def goalTest(problem,node):
    return node.state==problem.goal_state
def queuingFn(problem,nodes,node):
    for child in problem.graph[node.ID]:
        child.g=node.g+child.c
        child.p=node
        nodes.append(child)
    return nodes   

def bfs(problem,initial_node):
    nodes=deque([initial_node])
    while True:
        if not nodes:
            return Node(-1,"Failure")
        node=nodes.popleft() 
        if goalTest(problem,node):
            return node   
        nodes=queuingFn(problem,nodes,node)  
def printPath(node):
    if node.p==None:
        print(node.state,end=" ")
        return
    printPath(node.p)
    print(node.state,end=" ")               
def main():
    graph=[
        [Node(1,'a',c=5),Node(2,'b',c=2),Node(3,'c',c=4)],
        [Node(4,'d',c=9),Node(5,'e',c=4)],
        [Node(7,'g',c=6)],
        [Node(6,'f',c=2)],
        [Node(8,'h',c=7)],
        [Node(7,'g',c=6)],
        [Node(7,'g',c=1)],
        ]
    problem=Problem(graph,'s','g')
    initial_node=Node(0,'s',0,0,10000000)
    res=bfs(problem,initial_node) 
    print("Goal Node: ",res.state) 
    print("Path Cost: ",res.g) 
    printPath(res) 
main()