A = [[0,1,3],
		 [4,2,6],
		 [5,8,1],]
row,col = len(A),len(A[0])
step = row + col - 2

class Point():
		def __init__(self,loc):
				self.loc = loc
				self.dis = 0

graph = []
for i in range(row):
		tmp = []
		for j in range(col):
				tmp.append(Point([i,j]))
		graph.append(tmp)

#%%
for i in range(row):
		for j in range(col):
				if i==0 and j==0:
						graph[i][j].dis = 0
				elif i==0:
						graph[i][j].dis = graph[i][j-1].dis + A[i][j]
				elif j==0:
						graph[i][j].dis = graph[i-1][j].dis + A[i][j]
				else:
						graph[i][j].dis = min(graph[i-1][j].dis, graph[i][j-1].dis) + A[i][j]