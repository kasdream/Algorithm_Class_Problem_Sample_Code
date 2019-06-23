class Solution(object):
    def find_left_repeat_num(self,nums):
        d = {}
        
        res = []
        for i,num in enumerate(nums):
            if num in d:
                res.append(d[num])
            else:
                d[num] = i
                res.append(-1)
        return res
#x = Solution()
#print x.find_left_repeat_num([1,3,1,2,1])
