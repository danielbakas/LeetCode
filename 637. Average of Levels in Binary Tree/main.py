"""
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# 637. Average of Levels in Binary Tree | LeetCode
Program | `iterative.py`

Daniel Bakas <daniel@semanytk.com>

Difficulty: Easy
Topics: BFS, DFS

Given the root of a binary tree, return the average value of the nodes on
each level in the form of an array.

Oct 18, 2022
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
"""

# * Imports
# Package Imports
from collections import defaultdict
from typing import List


# * Main
# TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative
def iterative(root: TreeNode) -> List[float]:
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
def recursive(root: TreeNode) -> List[float]:
    counts = defaultdict(int)
    sums = defaultdict(int)

    def dfs(node: TreeNode = root, level: int = 0):
        if node:
            counts[level] += 1
            sums[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

    dfs()
    return [sums[i] / count for i, count in counts.items()]


# * Tests
result = TreeNode(3)
result.left = TreeNode(9)
result.right = TreeNode(20)
result.right.left = TreeNode(15)
result.right.right = TreeNode(7)
expected = [3.0, 14.5, 11.0]
assert iterative(result) == expected, "Test 1 (iterative): Failed"
assert recursive(result) == expected, "Test 1 (recursive): Failed"
print("Test 1: Passed")

# Test 2
result = TreeNode(1)
result.right = TreeNode(2)
expected = [1.0, 2.0]
assert iterative(result) == expected, "Test 2 (iterative): Failed"
assert recursive(result) == expected, "Test 2 (recursive): Failed"
print("Test 2: Passed")
