from bfs import BFS


class UndirectedConnectedComponents:
	def __init__(self, graph):
		self.graph = graph
		self.visited = set()
		self.ucc = []

	def __call__(self):
		for vertex in self.graph:
			if vertex not in self.visited:
				self.ucc.append(BFS(self.graph)(vertex))
				self.visited.update(self.ucc[-1])
		return self.ucc
