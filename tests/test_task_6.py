import pytest
from src.task_6 import dynamic_programming, greedy_algorithm


def test_dynamic_programming():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    budget = 100
    selected_items, total_cost, total_calories = dynamic_programming(items, budget)
    assert total_cost == 100
    assert total_calories == 970
    assert set(selected_items) == {"potato", "cola", "pepsi", "pizza"}


def test_greedy_algorithm():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    budget = 100
    selected_items, total_cost, total_calories = greedy_algorithm(items, budget)
    assert total_cost == 80
    assert total_calories == 870
    assert set(selected_items) == {"potato", "cola", "pepsi", "hot-dog"}
