from locks import Lock
from adjacency_list import AdjacencyList
from adjacency_matrix import AdjacencyMatrix
from part_2.bfs import BFS
from part_2.dfs import DFS


class Graph:
	def __init__(self, adj_list=True):
		self.__graph = AdjacencyList() if adj_list else AdjacencyMatrix()
		self.__lock = Lock()

	def add_edge(self, u, v, weight=1):
		self.__lock.writer_acquire()
		try:
			if self.__graph.has_edge(u, v):
				raise ValueError("Edge already exists")

			if isinstance(self.__graph, AdjacencyMatrix):
				self.__graph.add_edge(u, v, weight)
			else:
				self.__graph.add_edge(u, v)
		finally:
			self.__lock.writer_release()

	def remove_edge(self, u, v):
		self.__lock.writer_acquire()
		try:
			if not self.__graph.has_edge(u, v):
				raise ValueError("Edge does not exist")

			self.__graph.remove_edge(u, v)
		finally:
			self.__lock.writer_release()

	def get_neighbors(self, u):
		self.__lock.reader_acquire()
		result = self.__graph.graph[u]
		self.__lock.reader_release()
		return result

	@property
	def graph(self):
		self.__lock.reader_acquire()
		result = self.__graph.graph
		self.__lock.reader_release()
		return result


if __name__ == "__main__":
	g = Graph()
	g.add_edge(1, 2)
	g.add_edge(1, 3)
	g.add_edge(2, 3)
	g.add_edge(3, 4)
	g.add_edge(4, 1)
	print(g.graph)
	# g.remove_edge(4, 1)
	# g.remove_edge(3, 4)
	print(g.graph)
	print(g.get_neighbors(1))
	print(g.get_neighbors(2))
	print(g.get_neighbors(3))
	print(g.get_neighbors(4))

	bfs = BFS(g)
	print(bfs(2))

	dfs = DFS(g)
	print(dfs.dfs(2, recursive=True))

