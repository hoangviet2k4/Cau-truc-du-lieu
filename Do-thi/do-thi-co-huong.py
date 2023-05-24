class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].remove(vertex2)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for vertices in self.graph.values():
                if vertex in vertices:
                    vertices.remove(vertex)

    def print_graph(self):
        for vertex, neighbors in self.graph.items():
            if neighbors:
                for neighbor in neighbors:
                    print(vertex, "->", neighbor)
            else:
                print(vertex)


# Ví dụ
graph = Graph()

# Thêm các đỉnh
graph.add_vertex("4")
graph.add_vertex("6")
graph.add_vertex("12")
graph.add_vertex("9")
graph.add_vertex("10")

# Thêm các cạnh
graph.add_edge("4", "6")
graph.add_edge("6", "12")
graph.add_edge("12", "10")
graph.add_edge("10", "9")
graph.add_edge("9", "4")
graph.add_edge("9", "12")

# In đồ thị
graph.print_graph()
