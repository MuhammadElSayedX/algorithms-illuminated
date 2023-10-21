from collections import defaultdict


class AdjacencyList:
	def __init__(self):
		self.__graph = defaultdict(list)

	def add_edge(self, u, v):
		self.__graph[u].append(v)

	def remove_edge(self, u, v):
		self.__graph[u].remove(v)

	@property
	def graph(self):
		return self.__graph

	def has_edge(self, u, v):
		return v in self.__graph[u]
