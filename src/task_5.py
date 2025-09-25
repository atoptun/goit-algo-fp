import uuid
import networkx as nx
import matplotlib.pyplot as plt
import random
from rgb_gradient import get_linear_gradient
from collections import deque


class Node:
    """Binary tree node with color attribute for visualization"""
    def __init__(self, key, color="skyblue"):
        self.left: Node | None = None
        self.right: Node | None = None
        self.val = key
        self.color: str = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())

    def __str__(self) -> str:
        return f"Node({self.val}, {self.color})"


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


def draw_tree(tree_root: Node | None, title: str = "Binary Tree"):
    """Draws the binary tree"""
    if tree_root is None:
        print("Tree is empty.")
        return
    tree = nx.DiGraph()
    pos = {tree_root.id: (0.0, 0.0)}
    tree = add_edges(tree, tree_root, pos)

    shift = 1.0
    for k, (x, y) in pos.items():
        pos[k] = (x, y - shift)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def build_binary_tree(array: list[int]) -> Node | None:
    """Builds a binary tree from a array"""
    if not array:
        return None

    mid = len(array) // 2
    node = Node(array[mid])

    node.left = build_binary_tree(array[:mid])
    node.right = build_binary_tree(array[mid + 1:])

    return node


def dfs_preorder_tree(node: Node | None, colors: list[str]) -> list[Node] | None:
    if node is None:
        return []
    visited = []
    
    stack = [node]
    while stack:
        vertex = stack.pop()  
        vertex.color = colors.pop()
        visited.append(vertex)
        if vertex.right:
            stack.append(vertex.right)
        if vertex.left:
            stack.append(vertex.left)
    return visited


def bfs_preorder_tree(node: Node | None, colors: list[str]) -> list[Node] | None:
    if node is None:
        return
    visited = []
    
    queue = deque([node])
    while queue:
        vertex = queue.popleft()  
        vertex.color = colors.pop()
        visited.append(vertex)
        if vertex.left:
            queue.append(vertex.left)
        if vertex.right:
            queue.append(vertex.right)
    return visited


def main():
    array = [15, 91, 24, 19, 77, 22, 24, 62, 45, 26, 97, 53]
    # array = [random.randint(1, 100) for _ in range(12)]
    array.sort()
    root = build_binary_tree(array)
    print("Input array:", array)

    intermediate_colors = ["#95C9EB", "#0068AD"] # ["#2ff32f", "#114B11"]  # #1296F0
    colors = get_linear_gradient(colors=intermediate_colors, nb_colors=len(array), return_format='hex')
    dfs_order = dfs_preorder_tree(root, colors)
    line = " -> ".join(str(node) for node in dfs_order) if dfs_order else "None"
    print(f'DFS Preorder: {line}')
    draw_tree(root, title="DFS Preorder Traversal")

    intermediate_colors = ["#95C9EB", "#0068AD"] # ["#2ff32f", "#114B11"]  # #1296F0
    colors = get_linear_gradient(colors=intermediate_colors, nb_colors=len(array), return_format='hex')
    bfs_order = bfs_preorder_tree(root, colors)
    line = " -> ".join(str(node) for node in bfs_order) if bfs_order else "None"
    print(f'BFS Preorder: {line}')
    draw_tree(root, title="BFS Preorder Traversal")


if __name__ == "__main__":
    main()
