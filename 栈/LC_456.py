class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #边界条件
        if len(nums) < 3: return False
        stack = []
        for x in nums:
            #条件1,4
            if stack == [] or x < stack[-1][0]:
                stack.append([x,x])
            else:
                cur_min = stack[-1][0]
                #条件5
                while stack != [] and x >= stack[-1][1]:
                    stack.pop()
                
                #条件3
                if stack != [] and x > stack[-1][0] and x < stack[-1][1]:
                    return True
                #条件2
                stack.append([cur_min,x])
        return False
    
    
