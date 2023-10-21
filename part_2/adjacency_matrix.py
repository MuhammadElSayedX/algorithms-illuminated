from collections import defaultdict


class AdjacencyMatrix:
	def __init__(self):
		self.__graph = defaultdict(dict)

	def add_edge(self, u, v, weight=1):
		self.__graph[u][v] = weight

	def remove_edge(self, u, v):
		del self.__graph[u][v]

	@property
	def graph(self):
		return self.__graph

	def has_edge(self, u, v):
		return v in self.__graph[u]