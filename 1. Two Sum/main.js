/**
 * –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
 * # 1. Two Sum | LeetCode
 * Program | `main.js`
 *
 * Daniel Bakas <daniel@semanytk.com>
 *
 * Difficulty: Easy
 * Topics: Hash Map
 *
 * Given an array of integers nums and an integer target, return indices of the
 * two numbers such that they add up to target. You may assume that each input
 * would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
 *
 * Sep 4, 2022
 * ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
 */

//* Main
twoSum = (nums, target) => {
    let table = {};
    let expected;
    for (let [i, current] of Object.entries(nums)) {
        expected = target - current;
        if (expected in table)
            return [table[expected], i];
        table[current] = i;
    }
};

//* Tests
// Test 1
console.assert(`${twoSum([2, 7, 11, 15], 9)}` === `${[0, 1]}`);
console.log("Test 1: Passed");
// Test 2
console.assert(`${twoSum([3, 2, 4], 6)}` === `${[1, 2]}`);
console.log("Test 2: Passed");
// Test 3
console.assert(`${twoSum([3, 3], 6)}` === `${[0, 1]}`);
console.log("Test 3: Passed");