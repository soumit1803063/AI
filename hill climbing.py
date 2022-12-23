from math import inf
from random import randint
class Node:
	def __init__(self,ID=None,val=-inf):
		self.ID=ID
		self.val=val
class Problem:
	def __init__(self,graph=None):
		self.graph=graph


def EvaluationFn(node,problem):
	max_val=-inf
	candidates=[]
	if node.ID<=len(problem.graph):
		for successor in problem.graph[node.ID]:
			if successor.val>max_val:
				candidates=[]
				max_val=successor.val
			candidates.append(successor)
	if len(candidates)>0:
		return candidates[randint(0, len(candidates)-1)]
	return Node(-1)			
def hc(problem,curr_node):
	while True:
		next_node=EvaluationFn(curr_node,problem)
		if next_node.val<curr_node.val:
			return curr_node
		curr_node=next_node

def main():
	graph=[[Node(1,5)],
			[Node(2,6)],
			[Node(3,10)],
			[Node(4,13),Node(5,13)],
			[Node(6,5)],
			[Node(7,100)],
			]	

	problem=Problem(graph)	
	curr_node=Node(0,3)
	res=hc(problem, curr_node)
	print(res.ID)
	print(res.val)	
main()	