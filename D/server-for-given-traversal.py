import random

# Valid Colors
valid_colors = ["white", "black", "red", "green", "blue"]


# Represents a color token with a valid color
class ColorToken:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


# Represents an edge between two nodes
class Edge:
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b
        self.weight = random.randrange(0, 100)

    def get_weight(self):
        return self.weight

    def get_node_a(self):
        return self.node_a

    def get_node_b(self):
        return self.node_b

    def print_edge(self):
        return "(" + self.node_a.get_name() + "," + self.node_b.get_name() + "," + str(self.weight) + ")"


# Represents a node in the labyrinth
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.tokens = []

    def get_name(self):
        return self.name

    def get_tokens(self):
        return self.tokens

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def add_token(self, token):
        self.tokens.append(token)

    def get_neighbors(self):
        return self.neighbors


# Represent a set of all nodes connected through edges
class Tree:
    def __init__(self, node_name):
        self.parent = None
        self.node_name = node_name

    def get_node(self):
        return self.node_name

    def is_joined(self, tree):
        my_root = self.find_root().get_node()
        your_root = tree.find_root().get_node()
        return my_root == your_root

    def join(self, tree):
        tree.find_root().set_parent(self)

    def find_root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.find_root()

    def set_parent(self, new_parent):
        self.parent = new_parent


# A class to choose edges to connect all nodes using minimum spanning tree
class MinimumSpanningTree:
    def __init__(self, nodes, edges):
        self.tree_dict = {}
        # Sort edges according to their weight
        self.edges = sorted(edges, key=lambda edge: edge.get_weight())
        self.chosen_edges = []
        # Create a tree for each node
        for node in nodes:
            self.tree_dict[node.get_name()] = Tree(node.get_name())

    # Create the minimum spanning tree, return the list of edges used
    def create_tree(self):
        self.choose_edges()
        return self.chosen_edges

    # Choose edges to create minimum spanning tree using Kruskal's algorithm
    def choose_edges(self):
        for edge in self.edges:
            node_a = edge.get_node_a()
            node_b = edge.get_node_b()
            tree_a = self.tree_dict[node_a.get_name()]
            tree_b = self.tree_dict[node_b.get_name()]
            # Only use this edge if it doesn't create any cycle
            if not tree_a.is_joined(tree_b):
                tree_a.join(tree_b)
                self.chosen_edges.append(edge)
                node_a.add_neighbor(node_b)
                node_b.add_neighbor(node_a)


class Labyrinth:
    def __init__(self):
        # All color tokens currently placed, and where it's placed
        self.color_dict = {}
        # All edges in the graph
        self.Edges = []
        # All nodes in the graph
        self.Nodes = []

    # X is the width of the labyrinth and y is the height of the labyrinth. It uses nested for-loop to construct a
    # rectangle graph with named nodes. Implement Python module random and use it to choose a node randomly
    # and develop the labyrinth from there.
    def create_graph(self, x, y):
        if (x <= 0) or (y <= 0):
            raise Exception("Can't create labyrinth with negative or zero dimension")
        for width in range(x):
            for height in range(y):
                self.Nodes.append(Node(("(" + str(width) + "," + str(height) + ")")))
        self.generate_initial_edges()

    # Testing method, create graph with a random seed
    def create_graph_with_seed(self, x, y, seed):
        random.seed(seed)
        self.create_graph(x, y)

    # Create edges between each pair of nodes
    def generate_initial_edges(self):
        for nodeA in self.Nodes:
            for nodeB in self.Nodes:
                if not nodeA.get_name() == nodeB.get_name():
                    self.Edges.append(Edge(nodeA, nodeB))

    # Update edges to be edges forming minimum spanning tree connecting all nodes
    def minimal_spanning(self):
        mst = MinimumSpanningTree(self.Nodes, self.Edges)
        final_edges = mst.create_tree()
        self.Edges = final_edges

    # Return all edges as string
    def get_edges(self):
        edges = ""
        for edge in self.Edges:
            edges += edge.print_edge()
        return edges

    # Print out all nodes
    def get_nodes(self):
        nodes = ""
        for node in self.Nodes:
            nodes += node.get_name()
        return nodes

    # Add a color token to labyrinth
    def add_token(self, color, node):
        if (color in valid_colors) and (color not in self.color_dict):
            target_node = self.get_node(node)
            if target_node:
                target_node.add_token(ColorToken(color))
                self.color_dict[color] = target_node
            else:
                print("Node doesn't exist.")
        else:
            print("Invalid color.")

    # Find the Node object given the node name
    def get_node(self, node_name):
        for node in self.Nodes:
            if node.get_name() == node_name:
                return node
        return None

    # check if some colored token can reach some named graph node. In this method, using Breath First Search on the
    # node graph and return true if a path is found. The colored token's Node object should be the src parameter and
    # this function should return a boolean indicating whether the destination Node is reachable or not.
    def isReachable(self, src, dest):
        neighbors_to_check = []
        nodes_seen = []
        if src.get_name() == dest.get_name():
            return True
        else:
            neighbors_to_check.extend(src.get_neighbors())
            nodes_seen.append(src)
        while len(neighbors_to_check) > 0:
            current_node = neighbors_to_check.pop()
            if current_node.get_name() == dest.get_name():
                return True
            else:
                current_neighbors = current_node.get_neighbors()
                for neighbor in current_neighbors:
                    if neighbor not in nodes_seen:
                        neighbors_to_check.append(neighbor)
                nodes_seen.append(current_node)
        return False

    def is_color_reachable(self, color, node_name):
        if not (color in self.color_dict):
            print("Invalid color.")
        elif self.get_node(node_name) is None:
            print("Node doesn't exist.")
        else:
            return self.isReachable(self.color_dict[color], self.get_node(node_name))


if __name__ == "__main__":
    lab = Labyrinth()
    lab.create_graph_with_seed(3, 3, 100)
    lab.minimal_spanning()
    print(lab.get_nodes())
    print(lab.get_edges())
    lab.add_token("white", "(0,0)")
    print(lab.is_color_reachable("white", "(1,0)"))
