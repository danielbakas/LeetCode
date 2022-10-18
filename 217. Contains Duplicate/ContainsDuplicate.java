/**
 * –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
 * # 217. Contains Duplicate | LeetCode
 * Program | `ContainsDuplicate.java`
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

//* Imports
import java.util.Set;

//* Main
public class ContainsDuplicate {
    public static boolean containsDuplicate(int[] nums) {
        return nums.length == Set.of(nums).size();
    }

    public static void main(String[] args) {
        //* Tests
        // Test 1
        assert !containsDuplicate(new int[]{1, 2, 3});
        System.out.println("Test 1: Passed");
        // Test 2
        assert containsDuplicate(new int[]{1, 1});
        System.out.println("Test 2: Passed");
        // Test 3
        assert containsDuplicate(new int[]{1});
        System.out.println("Test 3: Passed");
    }
}