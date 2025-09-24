import networkx as nx
import matplotlib.pyplot as plt
import heapq


def show_graph(graph: dict[str, dict[str, int]]):
    G = nx.Graph()
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight)

    # Візуалізація графа
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


def dijkstra_net(graph: dict[str, dict[str, int]], start: str):
    G = nx.Graph()
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight)

    shortest_paths = nx.single_source_dijkstra_path(G, source=start)
    shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source=start)

    # print(f'Networkx: Shortest paths from node {start}:')
    # print(shortest_paths)

    return shortest_path_lengths


def print_table(distances, visited):
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)
    
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('inf'):
            distance = "∞"
        else:
            distance = str(distance)
        
        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")


def dijkstra(graph: dict[str, dict[str, int]], start: str) -> dict[str, int]:
    """Implementation of Dijkstra's algorithm"""
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()

    heap = [(0, start)]  # (distance, vertex)

    while heap:
        distance, cur_vertex = heapq.heappop(heap)
        if cur_vertex in visited:
            continue
        visited.add(cur_vertex)

        for neighbor, weight in graph[cur_vertex].items():
            if distances[cur_vertex] + weight < distances[neighbor]:
                distances[neighbor] = distances[cur_vertex] + weight
                heapq.heappush(heap, (distances[neighbor], neighbor))  # type: ignore

        # Вивід таблиці після кожного кроку
        # print_table(distances, visited)

    return distances  # type: ignore


def main():
    graph = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'D': 3},
        'C': {'A': 10, 'D': 2},
        'D': {'B': 3, 'C': 2, 'E': 4},
        'E': {'D': 4}
    }

    start_node = 'A'
    res = dijkstra(graph, start_node)
    print(f'Shortest paths from node {start_node}:\n', res)
    print('=' * 40)

    res_x = dijkstra_net(graph, start_node)
    print(f'Networkx: Shortest paths from node {start_node}:\n', res_x)

    show_graph(graph)


if __name__ == "__main__":
    main()
