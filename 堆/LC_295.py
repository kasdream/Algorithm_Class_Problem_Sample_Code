class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        #最大堆
        self.p1 = []
        #最小堆
        self.p2 = []
        
    #插入元素到堆中
    def insert_heap(self,heap,num):
        heapq.heappush(heap,num)
    
    #推出堆中元素
    def pop_heap(self,heap):
        return heapq.heappop(heap)
    
    
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.p1) == len(self.p2):
            #情况1
            #因为p1是最大堆，我们实现时用负数的话就相当于最小堆了
            self.insert_heap(self.p1,-num)
            num = -self.pop_heap(self.p1)
            self.insert_heap(self.p2,num)
        else:
            #情况2
            self.insert_heap(self.p2,num)
            num = self.pop_heap(self.p2)
            self.insert_heap(self.p1,-num)
            

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.p1) == len(self.p2):
            #情况1
            return (-self.p1[0]+self.p2[0])/2.
        else:
            #情况2
            return self.p2[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
