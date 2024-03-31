class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child, weight):
        self.children.append((child, weight))


root = Node("Début")
node1 = Node("Fils 1")
node2 = Node("Fils 2")
node3 = Node("fils 3")
node4 = Node("Fils_fin")

root.add_child(node1, 10)  
node1.add_child(node2, 10)  
node2.add_child(node4, 10) 
root.add_child(node4, 50) 
root.add_child(node3, 20) 
node3.add_child(node4, 20) 

print("Relations entre les nœuds :")
for node in [root, node1, node2, node3,node4]:
    print(f"{node.name} :")
    for child, weight in node.children:
        print(f"  -> {child.name} avec un poids de {weight}")


def shortest_path(start, end):
    visited = []
    queue = [(start, [start])]
    
    while queue:
        (node, path) = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node == end:
                return path
            for child, _ in node.children:
                if child not in visited:
                    queue.append((child, path + [child]))
    return None
# Calcul du chemin le plus court entre "Début" et "Fils_fin"
shortest_path_names = shortest_path(root, node4)

if shortest_path_names:
    shortest_path_node_names = []
    for node in shortest_path_names:
        shortest_path_node_names.append(node.name)
    print("Chemin le plus court entre Début et Fils_fin :", shortest_path_node_names)
else:
    print("Aucun chemin trouvé entre Début et Fils_fin.")


