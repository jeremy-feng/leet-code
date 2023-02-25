#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        # 求 A 的长度
        size_a = 0
        cur_a = headA
        while cur_a:
            cur_a = cur_a.next
            size_a += 1
        # 求 B 的长度
        size_b = 0
        cur_b = headB
        while cur_b:
            cur_b = cur_b.next
            size_b += 1
        # 初始化当前节点
        cur_a = headA
        cur_b = headB
        # 如果 a 比 b 短，则先将 b 向右移动
        if size_a < size_b:
            for _ in range(size_b - size_a):
                cur_b = cur_b.next
            # 同时向右移动，判断是否有相同节点
            for skip in range(size_a):
                if cur_a == cur_b:
                    return cur_a
                cur_a = cur_a.next
                cur_b = cur_b.next
        # 如果 a 比 b 长，则先将 a 向右移动
        elif size_a > size_b:
            for _ in range(size_a - size_b):
                cur_a = cur_a.next
            # 同时向右移动，判断是否有相同节点
            for skip in range(size_b):
                if cur_a == cur_b:
                    return cur_a
                cur_a = cur_a.next
                cur_b = cur_b.next
        # 如果一样长，则直接同时向右移动
        # 同时向右移动，判断是否有相同节点
        else:
            for skip in range(size_b):
                if cur_a == cur_b:
                    return cur_a
                cur_a = cur_a.next
                cur_b = cur_b.next
        return None


# @lc code=end
