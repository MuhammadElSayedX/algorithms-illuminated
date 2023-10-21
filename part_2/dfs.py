import copy


class DFS:
	def __init__(self, graph):
		self.__visited = set()
		self.__graph = graph.graph
		self.__stack = []

	def dfs(self, vertex, recursive=False):
		self._dfs_recursive(vertex) if recursive else self._dfs_iterative(vertex)
		visited = copy.deepcopy(self.__visited)
		self.__visited.clear()
		return visited

	def _dfs_recursive(self, vertex):
		self.__visited.add(vertex)
		for v in self.__graph[vertex]:
			if v not in self.__visited:
				self._dfs_recursive(v)

	def _dfs_iterative(self, vertex):
		self.__stack.append(vertex)
		while self.__stack:
			vertex = self.__stack.pop()
			if vertex not in self.__visited:
				self.__visited.add(vertex)
				for v in self.__graph[vertex]:
					self.__stack.append(v)
		return self.__visited
