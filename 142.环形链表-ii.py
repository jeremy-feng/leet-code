#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            # slow 前进 1 步
            slow = slow.next
            # fast 前进 2 步
            fast = fast.next.next
            # 如果相遇
            if slow == fast:
                # 从 head 开始跑一个
                index_1 = head
                # 从相遇节点开始跑一个
                index_2 = slow
                # 如果 index_1 和 index_2 没有相遇（他们应该在环行入口节点相遇）
                while index_1 != index_2:
                    # index_1 和 index_2 均前进 1 步
                    index_1 = index_1.next
                    index_2 = index_2.next
                # 退出 while 循环，说明已经相遇
                return index_1
        return None


# @lc code=end
