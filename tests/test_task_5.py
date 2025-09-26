import pytest
from src.task_5 import build_binary_tree, dfs_preorder_tree, bfs_preorder_tree


def test_build_binary_tree():
    array = [1, 2, 3, 4, 5, 6, 7]
    r = build_binary_tree(array)
    assert r is not None
    assert r.val == 4
    assert r.left is not None
    assert r.left.val == 2
    assert r.right is not None
    assert r.right.val == 6
    assert r.left.left is not None
    assert r.left.left.val == 1
    assert r.left.right is not None
    assert r.left.right.val == 3
    assert r.right.left is not None
    assert r.right.left.val == 5
    assert r.right.right is not None
    assert r.right.right.val == 7


def test_dfs_preorder_tree():
    array = [1, 2, 3, 4, 5, 6, 7]
    colors = [str(i) for i in range(len(array))]
    tree_root = build_binary_tree(array)
    result = dfs_preorder_tree(tree_root, colors=colors)
    result_vals = [node.val for node in result] if result is not None else []
    assert result_vals == [4, 2, 1, 3, 6, 5, 7]


def test_bfs_preorder_tree():
    array = [1, 2, 3, 4, 5, 6, 7]
    colors = [str(i) for i in range(len(array))]
    tree_root = build_binary_tree(array)
    result = bfs_preorder_tree(tree_root, colors=colors)
    result_vals = [node.val for node in result] if result is not None else []
    assert result_vals == [4, 2, 6, 1, 3, 5, 7]
