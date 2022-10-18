"""
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# 217. Contains Duplicate | LeetCode
Program | `contains_duplicate.py`

Daniel Bakas <daniel@semanytk.com>

Difficulty: Easy
Topics: Arrays

Given an integer array nums, return true if any value appears at least twice in
the array, and return false if every element is distinct.

Sep 19, 2022
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
"""

# * Imports
from typing import List


# * Main
def contains_duplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))


# * Tests
# Test 1
assert not contains_duplicate([1, 2, 3])
print("Test 1: Passed")
# Test 2
assert contains_duplicate([1, 1])
print("Test 2: Passed")
# Test 3
assert not contains_duplicate([1])
print("Test 3: Passed")
