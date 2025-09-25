import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import random


class Node:
    """Binary tree node with color attribute for visualization"""
    def __init__(self, key, color="skyblue"):
        self.left: Node | None = None
        self.right: Node | None = None
        self.val = key
        self.color: str = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


def add_edges(graph: nx.DiGraph, node: Node, pos: dict[str, tuple[float, float]], x=0, y=0, layer=1):
    """Recursively adds edges to the graph and calculates positions for visualization"""
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root: Node | None):
    """Draws the binary tree"""
    if tree_root is None:
        print("Tree is empty.")
        return
    tree = nx.DiGraph()
    pos = {tree_root.id: (0.0, 0.0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def build_tree_from_heap(array: list[int], index=0) -> Node | None:
    """Builds a binary tree from a heap array representation"""
    if index < len(array):
        node = Node(array[index])
        node.left = build_tree_from_heap(array, 2 * index + 1)
        node.right = build_tree_from_heap(array, 2 * index + 2)
        return node
    return None


def main():
    array = [15, 91, 24, 19, 77, 22, 24, 62, 45, 26, 97, 53]
    # array = [random.randint(1, 100) for _ in range(12)]
    print("Input array:", array)
    heapq.heapify(array)
    print("Min-heap:", array)
    root = build_tree_from_heap(array)

    # Відображення дерева
    draw_tree(root)


if __name__ == "__main__":
    main()
