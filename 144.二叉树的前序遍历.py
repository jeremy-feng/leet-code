#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#


# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.val)
            if root.left:
                res.extend(self.preorderTraversal(root.left))
            if root.right:
                res.extend(self.preorderTraversal(root.right))
        return res


root = TreeNode(
    val=0,
    left=None,
    right=TreeNode(
        val=2,
        left=TreeNode(val=3),
    ),
)
solution = Solution()
solution.preorderTraversal(root)
# @lc code=end
