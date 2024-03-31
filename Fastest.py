class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child, weight):
        self.children.append((child, weight))

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        self.graph[node.name] = {}

    def add_edge(self, from_node, to_node, weight):
        self.graph[from_node.name][to_node.name] = weight

    def dijkstra_fastest(self, start, destination):
        current = start
        to_visit = set(self.graph.keys()) - {start}
        distances = self.init_distances(start)
        previous_nodes = {}

        while current != destination:
            self.update_distances(current, distances, previous_nodes)
            current = self.get_new_current(to_visit, distances)
            if current is None:
                break

        return self.get_shortest_path(start, destination, previous_nodes)

    def init_distances(self, start):
        distances = {node: float('inf') for node in self.graph.keys()}
        distances[start] = 0
        return distances

    def update_distances(self, current, distances, previous_nodes):
        for neighbor, weight in self.graph[current].items():
            alternative_route = distances[current] + weight
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_nodes[neighbor] = current

    def get_new_current(self, to_visit, distances):
        min_dist = float('inf')
        new_current = None
        for node in to_visit:
            if distances[node] < min_dist:
                min_dist = distances[node]
                new_current = node

        if new_current:
            to_visit.remove(new_current)
        return new_current

    def get_shortest_path(self, start, destination, previous_nodes):
        path = []
        current = destination
        while current != start:
            path.append(current)
            current = previous_nodes[current]
        path.append(start)
        path.reverse()
        return path

if __name__=="__main__":
    # Création du graphe
    graph = Graph()

    root = Node("Début")
    node1 = Node("Fils 1")
    node2 = Node("Fils 2")
    node3 = Node("fils 3")
    node4 = Node("Fils_fin")

    # Ajout des nœuds au graphe
    graph.add_node(root)
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    graph.add_node(node4)

    # Ajout des arêtes avec les poids
    graph.add_edge(root, node1, 10)
    graph.add_edge(node1, node2, 10)
    graph.add_edge(node2, node4, 10)
    graph.add_edge(root, node4, 50)
    graph.add_edge(root, node3, 20)
    graph.add_edge(node3, node4, 20)

    # Exécution de l'algorithme de Dijkstra pour trouver le chemin le plus rapide entre "Début" et "Fils_fin"
    result = graph.dijkstra_fastest("Début", "Fils_fin")
    print("Chemin le plus rapide entre Début et Fils_fin :", result)

