from queue import PriorityQueue
from math import inf
class Node:
	def __init__(self,ID=None,state=None,c=None,h=None,g=inf,p=None):
		self.ID=ID
		self.state=state
		self.g=g
		self.c=c
		self.p=p
		self.h=h
	def __lt__(self, other):
		return ((self.g+self.h) < (other.g+other.h))
	
class Problem:
	def __init__(self,graph=None,initial_state=None,goal_state=None):
		self.graph=graph
		self.initial_state=initial_state
		self.goal_state=goal_state

def goalTest(problem,node):
	return problem.goal_state==node.state	

def queuingFn(nodes,node,problem):
	
	if node.ID< len(problem.graph): 
		for e in problem.graph[node.ID]:
			if e.g>e.c+node.g:
				e.g=e.c+node.g
				e.p=node
				nodes.put((e.g+e.h,e))
	return nodes
def printPath(node):
    if node.p==None:
        print(node.state,end=" ")
        return
    printPath(node.p)
    print(node.state,end=" ") 

def astar(problem,initial_node):
	nodes = PriorityQueue()
	nodes.put((initial_node.g+initial_node.h,initial_node))
	while True:
		if nodes.empty():
			return Node(-1,'Failure')
		node=nodes.get()[1]	
		if goalTest(problem, node):
			return node
		nodes=queuingFn(nodes, node, problem)	
			

def main():
	graph=[[Node(1,'b',4,12),Node(2,'c',3,11),],
	[Node(3,'f',6,11),Node(4,'e',12,4),],
	[Node(4,'e',10,4),Node(5,'d',7,6),],
	[Node(6,'g',16,0)],
	[Node(6,'g',5,0)],
	[Node(4,'e',2,4)],
			]
	problem=Problem(graph,'s','g')
	initial_node=Node(0,'s',0,14,0)
	res=astar(problem, initial_node)
	print("Goal Node: ",res.ID)
	print("Path Cost: ",res.g)
	printPath(res)
		
main()