import pytest
from src.task_3 import dijkstra, dijkstra_net


def test_dijkstra():
    graph = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'D': 3},
        'C': {'A': 10, 'D': 2},
        'D': {'B': 3, 'C': 2, 'E': 4},
        'E': {'D': 4}
    }
    start_node = 'A'
    expected_res = {
        'A': 0,
        'B': 5,
        'C': 10,
        'D': 8,
        'E': 12
    }
    assert dijkstra(graph, start_node) == dijkstra_net(graph, start_node) == expected_res


def test_dijkstra_2():
    graph = {
        'X': {'Y': 1, 'Z': 4},
        'Y': {'X': 1, 'Z': 2, 'W': 5},
        'Z': {'X': 4, 'Y': 2, 'W': 1},
        'W': {'Y': 5, 'Z': 1}
    }
    start_node = 'X'
    expected_res = {
        'X': 0,
        'Y': 1,
        'Z': 3,
        'W': 4
    }
    assert dijkstra(graph, start_node) == dijkstra_net(graph, start_node) == expected_res
