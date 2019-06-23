# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#递归解法
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #边界条件
        if head is None: return head
        if head.next is None: return head
        
        #取出下一个节点
        next_node = head.next
        #反转下一个节点开始的链表
        res = self.reverseList(next_node)
        #将头结点连回去
        next_node.next = head
        head.next = None
        #返回
        return res
    
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#非递归解法
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #边界条件
        if head is None: return head
        if head.next is None: return head
        
        #新建空结果链表
        res = None
        while not head is None:
            if res is None: 
                #如果结果链表为空，结果链表等于头结点
                res = head
                head = head.next
                res.next = None
            else:
                #如果结果链表不为空
                #先记录下一个节点
                tmp = head.next
                #将当前head连到结果链表
                head.next = res
                #更新结果链表头结点
                res = head
                #更新head
                head = tmp
            
        return res
        
