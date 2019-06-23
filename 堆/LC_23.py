# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #首先把所有链表头结点插入到堆中
        heap = []
        for head_node in lists:
            if head_node is None: continue
            #链表节点无法直接比较，我们将其val和其组成二元组，这样会以val大小来进行堆比较
            heapq.heappush(heap,(head_node.val,head_node))
        
        #定义返回的头和尾节点
        head = None
        tail = None
        #当堆不为空
        while not len(heap) == 0:
            #取出当前最小的节点
            val,now_node = heapq.heappop(heap)
            
            #将当前节点链接到我们的结果链表中
            if head is None: 
                head = now_node
                tail = now_node
            else:
                tail.next = now_node
                tail = now_node
                
            #获取当前节点的下一个节点
            next_node = tail.next
            tail.next = None
            
            #下一个节点插入堆中
            if not next_node is None:
                heapq.heappush(heap,(next_node.val,next_node))
        return head
