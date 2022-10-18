"""
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# 1. Two Sum | LeetCode
Program | `main.py`

Daniel Bakas <daniel@semanytk.com>

Difficulty: Easy
Topics: Hash Map

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target. You may assume that each input
would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Sep 3, 2022
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
"""

# * Imports
from typing import List


# * Main
def two_sum(nums: List[int], target: int) -> List[int]:
    table: dict = {}
    for i, current in enumerate(nums):
        expected = target - current
        if expected in table:
            return [table[expected], i]
        table[current] = i


# * Tests
# Test 1
assert two_sum([2, 7, 11, 15], 9) == [0, 1]
print("Test 1: Passed")
# Test 2
assert two_sum([3, 2, 4], 6) == [1, 2]
print("Test 2: Passed")
# Test 3
assert two_sum([3, 3], 6) == [0, 1]
print("Test 3: Passed")
