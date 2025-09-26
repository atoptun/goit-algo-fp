import pytest
from src.task_7 import dice_experiment


def test_dice_experiment():
    nums = 100000
    probabilities = dice_experiment(nums)
    assert abs(sum(probabilities.values()) - 1) < 0.01
    for face in range(2, 13):
        assert face in probabilities
        assert 0 <= probabilities[face] <= 1
