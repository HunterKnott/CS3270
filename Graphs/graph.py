'''Hunter Knott, Utah Valley University, CS 2420'''
import math
from queue import Queue

class Graph:
    '''A graph with vertices and directed/weighted edges'''
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, label):
        '''Adds a new vertex to the graph'''
        if not isinstance(label, str):
            raise ValueError("The label must be a string")
        self.adjacency_list[label] = []
        return self

    def add_edge(self, src, dest, w):
        '''Adds a new directed/weighted edge to the graph'''
        if len(src) > 1 or len(dest) > 1:
            raise ValueError("The source and destination labels must be a single character")
        if self.adjacency_list[src] is None:
            raise ValueError("The source vertex does not exist")
        if self.adjacency_list[dest] is None:
            raise ValueError("The destination index does not exist")
        if not isinstance(w, int) and not isinstance(w, float):
            raise ValueError("The weight must be a number")
        self.adjacency_list[src].append(dest)
        self.edge_weights[(src, dest)] = w
        return self

    def get_weight(self, src, dest):
        '''Returns an edge weight'''
        if self.adjacency_list[src] is None:
            raise ValueError("The source vertex does not exist")
        if self.adjacency_list[dest] is None:
            raise ValueError("The destination index does not exist")
        if dest not in self.adjacency_list[src]:
            return math.inf
        return self.edge_weights[(src, dest)]

    def dfs(self, src):
        '''Performs a depth-first traversal of the graph'''
        if src is None:
            raise ValueError("The given index does not exist")
        v_stack = [src]
        visited = []
        while len(v_stack) > 0:
            current_vertex = v_stack.pop()
            if current_vertex not in visited:
                visited.append(current_vertex)
                for adjacent_vertex in self.adjacency_list[current_vertex]:
                    v_stack.append(adjacent_vertex)
        return visited

    def bfs(self, src):
        '''Performs a breadth-first traversal of the graph'''
        if src is None:
            raise ValueError("The given index does not exist")
        discovered_set = set()
        frontier_queue = Queue()
        visited_list = []
        distances = dict()
        distances[src] = 0
        frontier_queue.put(src)
        discovered_set.add(src)
        while not frontier_queue.empty():
            current_vertex = frontier_queue.get()
            visited_list.append(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in discovered_set:
                    frontier_queue.put(adjacent_vertex)
                    discovered_set.add(adjacent_vertex)
                    distances[adjacent_vertex] = distances[current_vertex] + 1
        return visited_list

    def dsp(self, src, dest):
        '''Performs Dijkstr's shortest path from a start vertex to stop vertex'''
        # Breadth First for Dijkstra’s path: Get current, set weight of children,
        # set prev_vertex for children, add children to queue, move current node to visited,
        # set current as first in queue
        unvisited = self.adjacency_list

        # src.weight = 0
        # for child in src.edges.keys():
        #     queue.append(child)

        # # Add children to queue

        # # Start loop
        # while len(queue) > 0:
        #     current = self.graph[queue.pop(0)]

    def dsp_all(self, src):
        '''Performs Dijkstra's shortest path from a start vertex to all other vertices'''
        src = self.graph[src]

    def __str__(self):
        '''Returns a string representation of all vertices and edges'''
        graph_string = "digraph G {\n"
        for src_vertex in self.adjacency_list:
            for dest_vertex in self.adjacency_list[src_vertex]:
                edge_weight = str(self.get_weight(src_vertex, dest_vertex))
                graph_string += "   " + src_vertex + " -> " + dest_vertex + " [label=\"" + edge_weight + "\",weight=\"" + edge_weight + "\"];\n"
        graph_string += "}\n"
        return graph_string

def main():
    '''Used to test the graph'''
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", 2)
    g.add_edge("A", "F", 9)
    g.add_edge("B", "C", 8)
    g.add_edge("B", "D", 15)
    g.add_edge("B", "F", 6)
    g.add_edge("C", "D", 1)
    g.add_edge("E", "C", 7)
    g.add_edge("E", "D", 3)
    g.add_edge("F", "B", 6)
    g.add_edge("F", "E", 3)

    print(g)

    print("Starting DFS with vertex A")
    for vertex in g.dfs("A"):
        print(vertex, end="")
    print()

    print("Starting BFS with vertex A")
    for vertex in g.bfs("A"):
        print(vertex, end="")
    print()

if __name__ == "__main__":
    main()
