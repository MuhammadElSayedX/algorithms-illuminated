from main import Graph
from topo_sort import TopoSort


class StronglyConnectedComponents:
	def __init__(self, graph):
		self.graph = graph
		self.topo_sort = TopoSort(self.graph.reverse_graph())
		self.visited = set()
		self.scc = dict()
		self.num_scc = 0

	def dfs_scc(self, vertex, recursive=False):
		if recursive:
			self._dfs_scc_recursive(vertex)
		else:
			self._dfs_scc_iterative(vertex)

	def _dfs_scc_iterative(self, vertex):
		stack = [vertex]
		while stack:
			vertex = stack.pop()
			if vertex not in self.visited:
				self.visited.add(vertex)
				self.update_scc()
				for edge in self.graph.get_neighbors(vertex):
					stack.append(edge)

	def _dfs_scc_recursive(self, vertex):
		self.visited.add(vertex)
		self.update_scc()
		for edge in self.graph.get_neighbors(vertex):
			if edge not in self.visited:
				self._dfs_scc_recursive(edge)

	def update_scc(self):
		if self.num_scc not in self.scc:
			self.scc[self.num_scc] = 1
		else:
			self.scc[self.num_scc] += 1

	def kosaraju(self, recursive=False):
		f_function = self.topo_sort.sort()
		print(len(f_function))
		for index in range(1, len(f_function) + 1):
			vertex = f_function[index]
			if vertex not in self.visited:
				self.num_scc += 1
				self.dfs_scc(vertex, recursive)

	def top_scc(self, top=5):
		sorted_scc = sorted(self.scc.items(), key=lambda x: x[1], reverse=True)
		if top > len(sorted_scc):
			return sorted_scc + [0] * (top - len(sorted_scc))
		return sorted_scc[:top]


if __name__ == "__main__":
	graph_input = Graph(directed=True)

	with open("scc.txt", "r") as f:
		lines = f.readlines()
		for i in range(len(lines)):
			line = lines[i].split()
			graph_input.add_edge(line[0], line[1])
			if not graph_input.has_vertex(line[1]):
				graph_input.add_vertex(line[1])

	scc = StronglyConnectedComponents(graph_input)
	scc.kosaraju()

	print(scc.num_scc)
	print(scc.top_scc(5))
