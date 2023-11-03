class TopoSort:
	def __init__(self, graph):
		self.graph = graph
		self.current_label = len(self.graph)
		self.visited = set()
		self.f_func = dict()

	def sort(self, recursive=False):
		"""
		Topological sort of graph
		note::
			- In for loop the iter was `self.graph.get_vertices()` but it was not working
			as I get a `RuntimeError: dictionary changed size during iteration` so I changed
			it to `list(self.graph)`, but I'm working on the problem
		:param recursive: bool flag to use recursive approach
		:return: list of tuples (vertex, label)
		"""
		for vertex in list(self.graph):
			if vertex not in self.visited:
				self._dfs_topo(vertex, recursive)
		return self.f_func

	def _dfs_topo(self, vertex, recursive=False):
		if recursive:
			self._dfs_topo_recursive(vertex)
		else:
			self._dfs_topo_iterative(vertex)

	def _dfs_topo_recursive(self, vertex):
		self.visited.add(vertex)
		for neighbor in self.graph.get_neighbors(vertex):
			if neighbor not in self.visited:
				self._dfs_topo_recursive(neighbor)
		self.f_func[self.current_label] = vertex
		self.current_label -= 1

	def _dfs_topo_iterative(self, vertex):
		stack = [vertex]
		while stack:
			vertex = stack.pop()
			if vertex not in self.visited:
				self.visited.add(vertex)
				for neighbor in self.graph.get_neighbors(vertex):
					stack.append(neighbor)
				self.f_func[self.current_label] = vertex
				self.current_label -= 1

