from queue import PriorityQueue
from math import inf
class Node:
	def __init__(self,ID=None,state=None,h=None,c=None,g=inf,p=None):
		self.ID=ID
		self.state=state
		self.g=g
		self.c=c
		self.h=h
		self.p=p
class Problem:
	def __init__(self,graph=None,initial_state=None,goal_state=None,max_frontier_size=None):
		self.graph=graph
		self.initial_state=initial_state
		self.goal_state=goal_state
		self.max_frontier_size=max_frontier_size

def goalTest(problem,node):
	return problem.goal_state==node.state	

def queuingFn(nodes,node,problem):
	if node.ID<= len(problem.graph): 
		for e in problem.graph[node.ID]:
			e.g=e.c+node.g
			e.p=node
			nodes.put((e.h,e))
	temp_nodes=PriorityQueue()
	for i in range(problem.max_frontier_size):
		temp_nodes.put(nodes.get())	
	nodes=temp_nodes		
	return nodes



def beamSearch(problem,initial_node):
	nodes = PriorityQueue()
	nodes.put((initial_node.h,initial_node))
	while True:
		if nodes.empty():
			return Node(-1,'Failure')
		node=nodes.get()[1]	
		if goalTest(problem, node):
			return node
		nodes=queuingFn(nodes, node, problem)	

def printPath(node):
    if node.p==None:
        print(node.state,end=" ")
        return
    printPath(node.p)
    print(node.state,end=" ")  
def main():
	graph=[[Node(1,'a',8,1),Node(2,'b',4,5),Node(3,'c',3,8)],
			[Node(4,'d',inf,3),Node(5,'e',inf,7)],
			[Node(7,'g',0,4)],
			[Node(7,'g',0,4)],

			]

	max_frontier_size=1	
	problem=Problem(graph,'s','g',max_frontier_size)
	initial_node=Node(0,'s',8,0,0)
	res=beamSearch(problem, initial_node)
	print("Goal Node: ",res.ID)
	print("Path Cost: ",res.g)
	printPath(res)
		
main()