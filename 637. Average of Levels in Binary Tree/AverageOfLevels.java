/**
 * –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
 * # 637. Average of Levels in Binary Tree | LeetCode
 * Program | `AverageOfLevels.java`
 *
 * Daniel Bakas <daniel@semanytk.com>
 *
 * Difficulty: Easy
 * Topics: BFS, DFS
 *
 * Given the root of a binary tree, return the average value of the nodes on
 * each level in the form of an array.
 *
 * Oct 18, 2022
 * –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
 */

//* Imports
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

// Main Class
public class AverageOfLevels {
    // Iterative (BFS)
    public static List<Float> bfs(TreeNode root) {
        PriorityQueue<TreeNode> nodes = new PriorityQueue<TreeNode>();
        nodes.add(root);
        List<Float> averages = new ArrayList<>();
        while (!nodes.isEmpty()) {
            int amount = nodes.size();
            int total = 0;
            for (int i = 0; i < amount; i++) {
                TreeNode node = nodes.poll();
                if (node.left != null)
                    nodes.add(node.left);
                if (node.right != null)
                    nodes.add(node.left);
                total += node.val;
            }
            float average = (float) total / amount;
            averages.add(average);
        }
        return averages;
    }

    // Recursive (DFS)
    public static List<Float> dfs(TreeNode root) {
        List<Integer> sum = new ArrayList<>();
        List<Integer> count = new ArrayList<>();
        int level = 0;
        dfsRecursive(root, level, sum, count);
        List<Float> ans = new ArrayList<>();
        for (int i = 0; i < sum.size(); i++)
            ans.add((float) sum.get(i) / count.get(i));
        return ans;
    }

    private static void dfsRecursive(TreeNode node, int level,
                                     List<Integer> sum,
                                     List<Integer> count) {
        if (node == null) return;
        if (sum.size() == level) {
            count.add(0);
            sum.add(0);
        }
        count.set(level, count.get(level) + 1);
        sum.set(level, sum.get(level) + node.val);
        dfsRecursive(node.left, level + 1, sum, count);
        dfsRecursive(node.right, level + 1, sum, count);
    }

    //* Tests
    public static void main(String[] args) {
        TreeNode root;
        List<Float> expected;
        // Test 1
        root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);
        expected = new ArrayList<>();
        expected.add(3.0f);
        expected.add(14.5f);
        expected.add(11.0f);
        assert bfs(root) == expected;
        assert dfs(root) == expected;
        System.out.println("Test 1: Passed");
        // Test 2
        root = new TreeNode(1);
        root.right = new TreeNode(2);
        expected = new ArrayList<>();
        expected.add(1.0f);
        expected.add(2.0f);
        assert bfs(root) == expected;
        assert dfs(root) == expected;
        System.out.println("Test 2: Passed");
    }
}