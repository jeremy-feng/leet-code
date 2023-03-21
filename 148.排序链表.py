#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head  # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

    # def sortList(self, head):
    #     if not head:
    #         return head
    #     dummy = ListNode()
    #     dummy.next = head

    #     previous_were_sorted = head
    #     next_to_sort = head.next

    #     while next_to_sort:
    #         if next_to_sort.val >= previous_were_sorted.val:
    #             previous_were_sorted = previous_were_sorted.next
    #             next_to_sort = next_to_sort.next
    #         else:
    #             benchmark_1 = dummy
    #             benchmark_2 = dummy.next

    #             while True:
    #                 if benchmark_2.val >= next_to_sort.val:
    #                     previous_were_sorted.next = next_to_sort.next

    #                     next_to_sort.next = benchmark_2
    #                     benchmark_1.next = next_to_sort
    #                     next_to_sort = previous_were_sorted.next
    #                     break
    #                 else:
    #                     benchmark_1 = benchmark_1.next
    #                     benchmark_2 = benchmark_2.next
    #     return dummy.next


solution = Solution()
node_1 = ListNode(50000)
node_2 = ListNode(1)
node_3 = ListNode(2)
node_4 = ListNode(3)
node_5 = ListNode(4)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
solution.sortList(node_1)

# @lc code=end
