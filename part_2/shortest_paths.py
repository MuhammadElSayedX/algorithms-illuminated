import math
from queue import Queue

from graph_representation import Graph


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
        self.__distances = {vertex: float("inf") for vertex in graph}
        self.__distances[source] = 0
        queue = Queue()
        queue.put(source)
        while not queue.empty():
            vertex = queue.get()
            for neighbor in graph.get_neighbors(vertex):
                if self.__distances[neighbor] == float("inf"):
                    self.__distances[neighbor] = self.__distances[vertex] + 1
                    queue.put(neighbor)
        return self.__distances


class SingleSourceShortestPath:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.distances = dict()

    def dijkstra_algorithm(self, source, destination):
        self.visited.add(source)
        self.distances = {vertex: float("inf") for vertex in self.graph.get_vertices()}
        self.distances[source] = 0

        while destination not in self.visited:
            min_distance = float("inf")
            next_vertex = None

            for vertex in self.visited:
                remaining_edges = set(self.graph.get_neighbors(vertex)) - self.visited
                for edge in remaining_edges:
                    dist = self.distances[vertex] + self.graph.get_neighbors(vertex)[edge]
                    if min_distance > dist:
                        min_distance = dist
                        next_vertex = edge

            self.visited.add(next_vertex)
            self.distances[next_vertex] = min_distance

        return self.distances[destination]


if __name__ == "__main__":
    graph_input = Graph(weighted=True)

    with open("dijkstra's algorithm.txt", "r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            line = lines[i].split()
            for index in range(1, len(line)):
                edge, weight = line[index].split(",")
                graph_input.add_edge(line[0], edge, int(weight))

    destinations = ["7", "37", "59", "82", "99", "115", "133", "165", "188", "197"]
    for destination in destinations:
        shortest_path = SingleSourceShortestPath(graph=graph_input)
        print(shortest_path.dijkstra_algorithm("1", destination), end=",")
