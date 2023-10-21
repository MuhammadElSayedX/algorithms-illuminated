from bfs import BFS


class UCC:
	def __init__(self, graph):
		self.__graph = graph
		self.__visited = set()
		self.__ucc = []

	def __call__(self):
		for vertex in self.__graph.graph:
			if vertex not in self.__visited:
				self.__ucc.append(BFS(self.__graph)(vertex))
				self.__visited.update(self.__ucc[-1])
		return self.__ucc
