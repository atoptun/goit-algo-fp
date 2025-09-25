from pprint import pprint


def greedy_algorithm(items: dict, budget: int):
    """Greedy algorithm to maximize calories within budget"""
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']
    
    return selected_items, total_cost, total_calories


def dynamic_programming(items: dict, budget: int):
    """Dynamic programming approach to maximize calories within budget"""
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    item_list = list(items.items())
    
    for i in range(1, n + 1):
        item, info = item_list[i - 1]
        cost = info['cost']
        calories = info['calories']
        
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    w = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item, info = item_list[i - 1]
            selected_items.append(item)
            w -= info['cost']
    
    total_cost = sum(items[item]['cost'] for item in selected_items)
    total_calories = sum(items[item]['calories'] for item in selected_items)
    
    return selected_items, total_cost, total_calories


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    print('Available items:')
    pprint(items)
    print()
    
    budget = 100
    ga_selected_items, ga_total_cost, ga_total_calories = greedy_algorithm(items, budget)
    print(f"""Greedy Algorithm:
    Selected items: {ga_selected_items}
    Total cost: {ga_total_cost}
    Total calories: {ga_total_calories}
    """)

    dp_selected_items, dp_total_cost, dp_total_calories = dynamic_programming(items, budget)
    print(f"""Dynamic Programming:
    Selected items: {dp_selected_items}
    Total cost: {dp_total_cost}
    Total calories: {dp_total_calories}
    """)


if __name__ == "__main__":
    main()
