from graph_representation import Graph
from generic_graph_search import BreathFirstSearch, DepthFirstSearch

if __name__ == "__main__":

	g = Graph()
	g.add_edge(1, 2)
	g.add_edge(1, 3)
	g.add_edge(2, 3)
	g.add_edge(3, 4)
	g.add_edge(4, 1)
	print(g.graph)

	print(g.graph)
	print(g.get_neighbors(1))
	print(g.get_neighbors(2))
	print(g.get_neighbors(3))
	print(g.get_neighbors(4))

	bfs = BreathFirstSearch(g)
	print(bfs.search(2))

	dfs = DepthFirstSearch(g)
	print(dfs.search(2, recursive=True))

	graph = Graph(directed=True)
	graph.add_edge(1, 3)
	graph.add_edge(1, 5)
	graph.add_edge(2, 5)
	graph.add_edge(3, 2)
	graph.add_edge(3, 4)

	graph.add_vertex(4)
	graph.add_vertex(5)

	print(graph.graph)

	new_reversed_graph = graph.reverse_graph()
	print(new_reversed_graph.graph)
