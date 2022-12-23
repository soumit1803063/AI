
#incomplete code
#incomplete code
#incomplete code


from math import inf
from math import e
from random import randint
class Node:
	def __init__(self,ID=None,val=-inf,probability=1):
		self.ID=ID
		self.val=val
		self.probability=probability
class Problem:
	def __init__(self,graph=None):
		self.graph=graph


def get_successor(node,problem):
	if node.ID<len(problem.graph):
			return problem.graph[node.ID][randint(0, len(problem.graph[node.ID])-1)]		
	return Node(-1)			
def sa(problem,curr_node):
	T=15
	while True:
		T=T/2
		if T<1:
			return curr_node
		next_node=get_successor(curr_node,problem)
		E=next_node.val-curr_node.val
		if E>0:
			curr_node=next_node
		else:
			curr_node=next_node
			curr_node.probablity=e**(E*T)

def makeRandomGraph():
	data = list(range(1, 10000))
	random.shuffle(data)
	lst=[]
	i=0;
	j=randint(2, b)
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
	res=sa(problem, curr_node)
	print("maxima: ",res.ID)
	print("value",res.val)	
	print("probability",res.probability)
main()	