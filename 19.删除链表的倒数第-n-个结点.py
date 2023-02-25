#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_dummy = ListNode(next=head)
        slow = head_dummy
        fast = head_dummy
        # 将 fast 向右移动 n
        for _ in range(n):
            fast = fast.next
        # 只要 fast 不是最后一个节点，就将 slow 和 fast 均向右移动一个
        while fast.next:
            slow = slow.next
            fast = fast.next
        # 删除 slow 后面的一个节点
        slow.next = slow.next.next
        return head_dummy.next


# @lc code=end
