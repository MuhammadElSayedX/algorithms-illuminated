# Built-In Imports
import copy

from queue import Queue
from abc import ABC, abstractmethod


class GenericGraphSearch(ABC):
	"""
	Abstract class for graph search algorithms
	"""
	def __init__(self, graph):
		self.graph = graph
		self.visited = set()

	@abstractmethod
	def search(self, start):
		pass


class DepthFirstSearch(GenericGraphSearch):
	def __init__(self, graph):
		super().__init__(graph)
		self.stack = []

	def search(self, start, recursive=False):
		if recursive:
			self._dfs_recursive(start)
		else:
			self._dfs_iterative(start)

		visited = copy.deepcopy(self.visited)
		self.visited.clear()
		return visited

	def _dfs_recursive(self, vertex):
		self.visited.add(vertex)
		for v in self.graph.get_neighbors(vertex):
			if v not in self.visited:
				self._dfs_recursive(v)

	def _dfs_iterative(self, vertex):
		self.stack.append(vertex)
		while self.stack:
			vertex = self.stack.pop()
			if vertex not in self.visited:
				self.visited.add(vertex)
				for v in self.graph.get_neighbors(vertex):
					self.stack.append(v)


class BreathFirstSearch(GenericGraphSearch):
	def __init__(self, graph):
		super().__init__(graph)
		self.queue = Queue()

	def search(self, start):
		self.queue.put(start)

		while not self.queue.empty():
			vertex = self.queue.get()
			if vertex not in self.visited:
				self.visited.add(vertex)
				for neighbor in self.graph.get_neighbors(vertex):
					self.queue.put(neighbor)

		return self.visited
