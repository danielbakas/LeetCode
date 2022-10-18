/**
 * –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
 * # 217. Contains Duplicate | LeetCode
 * Program | `containsDuplicate.js`
 *
 * Daniel Bakas <daniel@semanytk.com>
 *
 * Difficulty: Easy
 * Topics: Arrays
 *
 * Given an integer array nums, return true if any value appears at least
 * twice in the array, and return false if every element is distinct.
 *
 * Oct 18, 2022
 * –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
 */

//* Main
containsDuplicate = (nums) => { return nums.length !== new Set(nums).size }

//* Tests
// Test 1
console.assert(!containsDuplicate([1, 2, 3]));
console.log("Test 1: Passed");
// Test 2
console.assert(containsDuplicate([1, 1]));
console.log("Test 2: Passed");
// Test 3
console.assert(!containsDuplicate([1]));
console.log("Test 3: Passed");