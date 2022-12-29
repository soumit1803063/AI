from collections import deque 
from math import inf

class Node:
    def __init__(self,ID,state=None,g1=inf,g2=inf,c=None,p1=None,p2=None):
        self.ID=ID
        self.state=state
        self.g1=g1
        self.g2=g2
        self.c=c
        self.p1=p1
        self.p2=p2
class Problem:
    def __init__(self,graph,initial_state,goal_state):
        self.graph=graph
        self.initial_state=initial_state
        self.goal_state=goal_state
def intersectionTest(visited1,visited2):
	for i in range(len(visited1)):
		if visited1[i] is not None and visited2[i] is not None:
			visited1[i].p2=visited2[i].p2
			visited1[i].g2=visited2[i].g2
			return visited1[i]
	return None
def queuingFn(problem,nodes,node,visited,direction):
    if node.ID< len(problem.graph):
        for child in problem.graph[node.ID]:
  
            if direction==True: #start to goal
            	child.p1=node
            	child.g1=node.g1+child.c
            else:
            	child.p2=node #goal to start
            	child.g2=node.g2+child.c
            
            nodes.append(child)
            visited[child.ID]=child
    return nodes,visited   

def bbfs(problem,initial_node,goal_node):
    visited1=[None]*len(problem.graph)
    visited2=[None]*len(problem.graph)
    nodes1=deque([initial_node])
    nodes2=deque([goal_node])
    visited1[initial_node.ID]=initial_node
    visited2[goal_node.ID]=goal_node
    while True:
        if (not nodes1) or (not nodes2):
            return Node(-1,"Failure")
        node1=nodes1.popleft()
        node2=nodes2.popleft()  
        ret = intersectionTest(visited1,visited2)
        if ret:
            return ret  
        nodes1,visited1=queuingFn(problem,nodes1,node1,visited1,direction=True) 
        nodes2,visited2=queuingFn(problem,nodes2,node2,visited2,direction=False)  
def printPath1(node):
    if node.p1==None:
        print(node.state,end=" ")
        return
    printPath1(node.p1)
    print(node.state,end=" ")
def printPath2(node):
    if node.p2==None:
        print(node.state,end=" ")
        return
    print(node.state,end=" ")      
    printPath2(node.p2)

def main():
	#undirected graph
    graph=[
        [Node(1,'a',c=5),Node(2,'b',c=2),Node(3,'c',c=4)],#0
        [Node(4,'d',c=9),Node(5,'e',c=4),Node(0,'s',c=5)],#1
        [Node(7,'g',c=6),Node(0,'s',c=2)],#2
        [Node(6,'f',c=2),Node(0,'s',c=4)],#3
        [Node(8,'h',c=7),Node(1,'a',c=9)],#4
        [Node(7,'g',c=6),Node(1,'a',c=9)],#5
        [Node(7,'g',c=1),Node(3,'c',c=2)],#6
        [Node(2,'b',c=6),Node(5,'e',c=6),Node(6,'f',c=1)],#7
        [Node(4,'d',c=7)]#8
        ]
    problem=Problem(graph,'s','g')
    initial_node=Node(ID=0,state='s',g1=0,g2=inf,c=0,p1=None,p2=None)
    goal_node=Node(ID=7,state='g',g1=inf,g2=0,c=0,p1=None,p2=None)
    res=bbfs(problem,initial_node,goal_node) 
    print("Goal Node: ",goal_node.state) 
    print("Path Cost: ",res.g1+res.g2) 
    printPath1(res) 
    printPath2(res.p2) 

main()