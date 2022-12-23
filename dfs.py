from math import inf
class Node:
	def __init__(self,ID=None,state=None,c=None,g=inf,p=None):
		self.ID=ID
		self.state=state
		self.g=g
		self.c=c
		self.p=p
class Problem:
	def __init__(self,graph=None,initial_state=None,goal_state=None):
		self.graph=graph
		self.initial_state=initial_state
		self.goal_state=goal_state

def goalTest(problem,node):
	return problem.goal_state==node.state	

def queuingFn(nodes,node,problem):
	if node.ID<= len(problem.graph): 
		for e in problem.graph[node.ID]:
			e.g=e.c+node.g
			e.p=node
			nodes.append(e)
	return nodes

def printPath(node):
    if node.p==None:
        print(node.state,end=" ")
        return
    printPath(node.p)
    print(node.state,end=" ") 

def dfs(problem,initial_node):
	nodes =[]
	nodes.append(initial_node)
	while True:
		if len(nodes)==0:
			return Node(-1,'Failure')
		node=nodes.pop()
		if goalTest(problem, node):
			return node
		nodes=queuingFn(nodes, node, problem)	
				

def main():
	graph=[[Node(1,'a',5),Node(2,'b',2),Node(3,'c',4)],
			[Node(4,'d',9),Node(5,'e',4)],
			[Node(7,'g',6)],
			[Node(6,'f',2)],
			[Node(8,'h',9)],
			[Node(7,'g',6)],
			[Node(7,'g',1)],
			]
	problem=Problem(graph,'s','g')
	initial_node=Node(0,'s',0,0)
	res=dfs(problem, initial_node)
	print("Goal Node: ",res.ID)
	print("Path Cost: ",res.g)
	printPath(res)
		
main()