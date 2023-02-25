#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # 创建虚拟头节点
        dummy = ListNode(next=head)
        # 找到反转链表的左边一个值，即 1
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        # 反转部分链表
        left_node = pre.next
        pre_ = None
        cur_ = left_node
        for _ in range(right - left + 1):
            tmp = cur_.next
            cur_.next = pre_
            pre_ = cur_
            cur_ = tmp
        # 将 2 指向 5
        left_node.next = cur_
        # 将 1 指向 4
        pre.next = pre_
        return dummy.next


# @lc code=end
