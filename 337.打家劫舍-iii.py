#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def travel(node):
            if node is None:
                return (0, 0)
            # 计算：如果到了左子结点的话，偷与不偷左子结点的金额
            left = travel(node.left)
            # 计算：如果到了右子结点的话，偷与不偷右子结点的金额
            right = travel(node.right)
            # 计算：如果偷本结点，不偷子结点，则在本结点能拿到的金额为：本结点的金额 + 在左结点但不偷左结点的金额 + 在右结点但不偷右结点的金额
            steel_current = node.val + left[1] + right[1]
            # 如果不偷本结点，直接到子结点，则在本结点能拿到的金额为：在左结点，且可以选择偷或不偷左结点的金额的最大值 + 在右结点，且可以选择偷或不偷右结点的金额的最大值
            steel_child = max(left[0], left[1]) + max(right[0], right[1])
            return steel_current, steel_child

        return max(travel(root))


# @lc code=end
