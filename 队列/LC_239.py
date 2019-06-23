class Solution(object):
    
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        #定义插入一个数的操作，输入是(时间戳，数字)
        def add(i,num):
            #判断队首是否应该出队
            if len(q) != 0 and q[0][0] == i-k:
                q.popleft()
            #判断队尾是否应该出队
            while (len(q) != 0 and num >= q[-1][1]):
                q.pop()
            #插入新二元组
            q.append((i,num))
            
            #返回队首，即当前最大值
            return q[0][1]
        q = deque()
        
        res = []
        for i,num in enumerate(nums):
            res.append(add(i,num))
        
        #结果只保留k-1往后的，前面的结果都不到k个数
        return res[k-1:]
