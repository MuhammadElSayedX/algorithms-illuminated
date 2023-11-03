# Built-In Imports
from collections import defaultdict
from abc import ABC, abstractmethod


class GraphAbstractRepresentation(ABC):
	def __init__(self, directed=False, weight=1):
		"""
		Fundamental graph representation class
		:param directed: flag to indicate if the graph is directed
		:param weight: weight of the graph edges
		"""
		self.graph = defaultdict(dict) | defaultdict(list)
		self.directed = directed
		self.weighted = weight

	@abstractmethod
	def add_edge(self, u, v, weight=1):
		pass

	@abstractmethod
	def add_vertex(self, v):
		pass

	@abstractmethod
	def remove_edge(self, u, v):
		pass

	@abstractmethod
	def get_neighbors(self, u):
		pass

	@abstractmethod
	def reverse_graph(self):
		pass

	def reverse_helper(self, reversed_graph):
		if not self.directed:
			raise ValueError("Graph is not directed")

		for v in self.graph.keys():
			if v not in reversed_graph.graph:
				reversed_graph.add_vertex(v)

			for u in self.get_neighbors(v):
				reversed_graph.add_edge(u, v)

		return reversed_graph

	def has_edge(self, u, v):
		return v in self.graph[u]

	def has_vertex(self, v):
		return v in self.graph

	def get_vertices(self):
		return self.graph.keys()

	def __str__(self):
		return str(self.graph)

	def __len__(self):
		return len(self.graph)

	def __iter__(self):
		return iter(self.graph)


class AdjacencyList(GraphAbstractRepresentation):
	"""
	Adjacency list representation of a graph
	note::
		- weights are not supported in this representation, yet.
	"""
	def __init__(self, directed=False, weight=1):
		super().__init__(directed, weight)
		self.graph = defaultdict(list)

	def add_edge(self, u, v, weight=1):
		self.graph[u].append(v)
		if not self.directed:
			self.graph[v].append(u)

	def add_vertex(self, v):
		self.graph[v] = []

	def remove_edge(self, u, v):
		self.graph[u].remove(v)
		if not self.directed:
			self.graph[v].remove(u)

	def get_neighbors(self, u):
		return self.graph[u]

	def reverse_graph(self):
		return self.reverse_helper(AdjacencyList(directed=True))


class AdjacencyMatrix(GraphAbstractRepresentation):
	"""
	Adjacency matrix representation of a graph
	"""
	def __init__(self, directed=False, weight=1):
		super().__init__(directed, weight)
		self.graph = defaultdict(dict)

	def add_edge(self, u, v, weight=1):
		self.graph[u][v] = weight
		if not self.directed:
			self.graph[v][u] = weight

	def add_vertex(self, v):
		self.graph[v] = dict()

	def remove_edge(self, u, v):
		del self.graph[u][v]
		if not self.directed:
			del self.graph[v][u]

	def get_neighbors(self, u):
		return self.graph[u].keys()

	def reverse_graph(self):
		return self.reverse_helper(AdjacencyMatrix(directed=True))


class Graph:
	"""
	Graph class that uses the adjacency list representation by default
	note::
		- Graph class isn't thread safe, yet!
	"""
	def __init__(self, representation=AdjacencyList, directed=False, weight=1):
		self.representation = representation(directed, weight)
		self.graph = self.representation.graph

	def add_edge(self, u, v, weight=1):
		self.representation.add_edge(u, v, weight)

	def add_vertex(self, v):
		self.representation.add_vertex(v)

	def remove_edge(self, u, v):
		self.representation.remove_edge(u, v)

	def has_edge(self, u, v):
		return self.representation.has_edge(u, v)

	def has_vertex(self, v):
		return self.representation.has_vertex(v)

	def get_vertices(self):
		return self.representation.get_vertices()

	def get_neighbors(self, u):
		return self.representation.get_neighbors(u)

	def reverse_graph(self):
		return self.representation.reverse_graph()

	def __len__(self):
		return len(self.representation)
