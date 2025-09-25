from collections import defaultdict
import matplotlib.pyplot as plt
import random
from tabulate import tabulate


def dice_experiment(nums: int) -> dict[int, float]:
    """Simulates rolling two dice 'nums' times and returns the probability distribution of their sums."""
    counts = defaultdict(int)
    for _ in range(nums):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        counts[roll1 + roll2] += 1

    return {face: count / nums for face, count in counts.items()}


def plot_probabilities(probabilities: dict[int, float]):
    """Plots the probability distribution of sums from two dice rolls."""
    faces = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(faces, probs, color='blue', alpha=0.7, tick_label=faces)
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Probability')
    plt.title('Probability Distribution of Sums from Two Dice Rolls')
    plt.xticks(faces)
    plt.ylim(0, max(probs) * 1.1)
    plt.grid(axis='y')
    plt.show()


def main():
    nums = [1000, 10_000, 100_000, 1_000_000, 10_000_000]
    results = {0: {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}}
    for n in nums:
        probabilities = dice_experiment(n)
        results[n] = probabilities

    tabs = [['Sum', 'Calc'] + [f"{n}" for n in results]]
    [tabs.append([str(s)]) for s in range(2, 13)]
    for n, probs in results.items():
        for key, prob in probs.items():
            tabs[key - 1].append(prob) # type: ignore

    print(tabulate(tabs, headers='firstrow', floatfmt=".4%", numalign="decimal", tablefmt="pipe"))

    plot_probabilities(results[nums[-1]])


if __name__ == "__main__":
    main()
