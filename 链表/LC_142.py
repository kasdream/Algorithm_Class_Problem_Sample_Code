# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #边界条件，视频中边界条件不完全，以代码为准。
        if head is None: return None
        if head.next is None: return None
        if head.next.next is None: return None
        
        #定义快慢指针
        a = head.next; b = head.next.next
        #快慢指针运行直到相遇
        while (not a is None and not b is None):
            if a == b: break
            a = a.next
            b = b.next
            if not b is None: b = b.next
        #如果a或者b有一个为None，表示没有环
        if a is None or b is None:
            return None
        #按所讲算法，寻找相遇点
        b = head
        while (a != b):
            a = a.next
            b = b.next
        return a
            
