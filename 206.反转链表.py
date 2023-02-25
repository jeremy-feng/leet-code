#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur != None:
            # 临时存储 cur.next
            tmp = cur.next
            # 局部反转
            cur.next = pre
            # 将 pre 和 cur 向右移动
            pre = cur
            cur = tmp
        return pre


# @lc code=end
# 双指针法：pre 在左，初始为 None，cur 在右，初始为 head。
