#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
# 定义单链表
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):
    def __init__(self):
        # 创建虚拟头节点
        self.head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        # 如果 index 大于链表长度，则不会插入节点
        if index > self.size:
            return
        # 如果 index 小于 0，则在头部插入节点
        if index < 0:
            index = 0
        cur = self.head
        for _ in range(index):
            cur = cur.next
        new_node = ListNode(val=val, next=cur.next)
        cur.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= 0 and index < self.size:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            cur.next = cur.next.next
            # 这个地方害我卡了很久！！！
            # 一定要注意，必须进入判断之后，才能运行 self.size -= 1
            # 千万不要无论如何都执行 self.size -= 1
            # 要检查缩进！！！
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index, val)
# obj.deleteAtIndex(index)
# @lc code=end
