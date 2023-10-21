from queue import Queue


class BFS:
	def __init__(self, graph):
		self.__graph = graph
		self.__queue = Queue()

	def __call__(self, start):
		self.__queue.put(start)
		visited = set()
		while not self.__queue.empty():
			vertex = self.__queue.get()
			if vertex not in visited:
				visited.add(vertex)
				for neighbor in self.__graph.get_neighbors(vertex):
					self.__queue.put(neighbor)
		return visited
