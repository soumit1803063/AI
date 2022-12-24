# #incomplete




# #incomplete
# from collections import deque 
# from math import inf
# class Node:
#     def __init__(self,ID,state=None,g=inf,h=None,c=None,p1=None,p2=None):
#         self.ID=ID
#         self.state=state
#         self.g=g
#         self.h=h
#         self.c=c
#         self.p1=p1
#         self.p2=p2
# class Problem:
#     def __init__(self,graph,initial_state,goal_state):
#         self.graph=graph
#         self.initial_state=initial_state
#         self.goal_state=goal_state
# def goalTest1(problem,node):
#     return node.state==problem.goal_state
# def goalTest2(problem,node):
#     return node.state==problem.initial_state
# def queuingFn(problem,nodes,node,vis,direction=True):
#     if node.ID< len(problem.graph):
#         for child in problem.graph[node.ID]:
#             child.g=node.g+child.c
#             if(direction==True):
#                 child.p1=node
#             else
#                 child.p2=node    
#             nodes.append(child)
#             vis[child.ID]=child
#     return nodes,vis   

# def bbfs(problem,initial_node,goal_node):
#     vis1=[None,None,None,None,None,None,None,None]
#     vis2=[None,None,None,None,None,None,None,None]
#     nodes1=deque([initial_node])
#     nodes2=deque([goal_node])
#     vis1[initial_node.ID]=
#     vis2[goal_node.ID]=1
#     while True:
#         if (not nodes1) or (not nodes2):
#             return Node(-1,"Failure")
#         node1=nodes1.popleft() nodes1,vis1=queuingFn(problem,nodes1,node1,vis1)
#         node2=nodes2.popleft()
#         for i in range(len(vis1)):
#             if vis1[i]==vis2[i]
#             return        
#         nodes1,vis1=queuingFn(problem,nodes1,node1,vis1,True)
#         nodes2,vis2=queuingFn(problem,nodes2,node2,vis2,False)  
        
# def printPath(node):
#     if node.p==None:
#         print(node.state,end=" ")
#         return
#     printPath(node.p)
#     print(node.state,end=" ")               
# def main():
#     #undirected graph
#     graph=[
#         [Node(1,'a',c=5),Node(2,'b',c=2),Node(3,'c',c=4)],#0
#         [Node(4,'d',c=9),Node(5,'e',c=4),Node(0,'s',c=5)],#1
#         [Node(7,'g',c=6),Node(0,'s',c=2)],#2
#         [Node(6,'f',c=2),Node(0,'s',c=4)],#3
#         [Node(8,'h',c=7),Node(1,'a',c=9)],#4
#         [Node(7,'g',c=6),Node(1,'a',c=9)],#5
#         [Node(7,'g',c=1),Node(3,'c',c=2)],#6
#         [Node(2,'b',c=6),Node(5,'e',c=6),Node(6,'f',c=1)]#7,
#         [Node(4,'d',c=7)]#8
#         ]
#     problem=Problem(graph,'s','g')
#     initial_node=Node(0,'s',0,0,0)
#     goal_node=Node(0,'g',0,0,0)
#     res=bbfs(problem,initial_node,goal_node) 
#     print("Goal Node: ",res.state) 
#     print("Path Cost: ",res.g) 
#     printPath(res) 
# main()