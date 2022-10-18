/**
 * –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
 * # 1. Two Sum | LeetCode <p/>
 * Program | `main.js` <p/>
 *
 * Daniel Bakas <daniel@semanytk.com> <p/>
 *
 * Difficulty: Easy
 * Topics: Hash Map
 *
 * Given an array of integers nums and an integer target, return indices of the
 * two numbers such that they add up to target. You may assume that each input
 * would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order. <p/>
 *
 * Sep 4, 2022
 * –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
 */

//* Imports
import java.util.HashMap;

//* Main
public class Main {
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> table = new HashMap<>();
        int[] result = new int[2];
        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];
            int expected = target - current;
            if (table.containsKey(expected))
                return new int[]{table.get(expected), i};
            table.put(current, i);
        }
        return result;
    }

    public static void main(String[] args) {
        //* Tests
        // Test 1
        assert twoSum(new int[]{2, 7, 11, 15}, 9) == new int[]{0, 1};
        System.out.println("Test 1: Passed");
        // Test 2
        assert twoSum(new int[]{3, 2, 4}, 6) == new int[]{1, 2};
        System.out.println("Test 2: Passed");
        // Test 3
        assert twoSum(new int[]{3, 3}, 6) == new int[]{0, 1};
        System.out.println("Test 3: Passed");
    }
}