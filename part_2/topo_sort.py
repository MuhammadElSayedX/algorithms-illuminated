class TopologicalSort:
	def __init__(self, graph):
		self.__graph = graph.graph
		self.current_label = len(self.__graph)
		self.visited = set()
		self.f_function = list()

	@property
	def graph(self):
		return self.__graph

	def topo_sort(self):
		for vertex in self.__graph:
			if vertex not in self.visited:
				self._dfs(vertex)
		return self.f_function

	def _dfs(self, vertex):
		self.visited.add(vertex)
		for neighbor in self.__graph[vertex]:
			if neighbor not in self.visited:
				self._dfs(neighbor)
		self.f_function.append((vertex, self.current_label))
		self.current_label -= 1
