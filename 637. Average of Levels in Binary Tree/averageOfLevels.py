"""
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# 637. Average of Levels in Binary Tree | LeetCode
Program | `averageOfLevels.py`

Daniel Bakas <daniel@semanytk.com>

Difficulty: Easy
Topics: BFS, DFS

Given the root of a binary tree, return the average value of the nodes on
each level in the form of an array.

Oct 18, 2022
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
"""

# * Imports
# Package Imports
from collections import defaultdict
from typing import List

# Project Imports
from util.TreeNode import TreeNode


# * Main
# Iterative
def bfs(root: TreeNode) -> List[float]:
    nodes: List[TreeNode] = [root]
    averages = []
    while nodes:
        amount: int = len(nodes)
        total: int = 0
        for _ in range(amount):
            node: TreeNode = nodes.pop(0)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            total += node.val
        averages.append(total / amount)
    return averages


# Recursive
def dfs(root: TreeNode) -> List[float]:
    counts = defaultdict(int)
    sums = defaultdict(int)

    def dfs_recursive(node: TreeNode = root, level: int = 0):
        if node:
            counts[level] += 1
            sums[level] += node.val
            dfs_recursive(node.left, level + 1)
            dfs_recursive(node.right, level + 1)

    dfs_recursive()
    return [sums[i] / count for i, count in counts.items()]


# * Tests
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
expected = [3.0, 14.5, 11.0]
assert bfs(root) == expected, "Test 1 (iterative): Failed"
assert dfs(root) == expected, "Test 1 (recursive): Failed"
print("Test 1: Passed")

# Test 2
root = TreeNode(1)
root.right = TreeNode(2)
expected = [1.0, 2.0]
assert bfs(root) == expected, "Test 2 (iterative): Failed"
assert dfs(root) == expected, "Test 2 (recursive): Failed"
print("Test 2: Passed")
