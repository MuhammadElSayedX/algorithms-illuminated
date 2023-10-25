import math
from queue import Queue


class ShortestPaths:
	def __init__(self, graph):
		self.__distances = {}
		self.graph = graph.graph

	def shortest_path(self, vertex):
		visited = set(vertex)
		length = {k: math.inf for k in self.graph}
		length[vertex] = 0
		queue = Queue()
		queue.put(vertex)
		while not queue.empty():
			vertex = queue.get()
			for edge in self.graph[vertex]:
				if edge not in visited:
					visited.add(edge)
					length[edge] = length[vertex] + 1
					queue.put(edge)
		return length

	def __call__(self, graph, source):
		self.__distances = {vertex: float('inf') for vertex in graph.graph}
		self.__distances[source] = 0
		queue = Queue()
		queue.put(source)
		while not queue.empty():
			vertex = queue.get()
			for neighbor in graph.get_neighbors(vertex):
				if self.__distances[neighbor] == float('inf'):
					self.__distances[neighbor] = self.__distances[vertex] + 1
					queue.put(neighbor)
		return self.__distances
