class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def dfs(l,r):
            #非法条件l>r
            if l > r : return -1
            #边界条件
            if r-l+1 <= 2: 
                if nums[l] == target: return l
                if nums[r] == target: return r
                return -1
            
            #取中点m
            m = (l+r) // 2
            #如果中点m的值等于目标值，返回m
            if target == nums[m]: return m
            
            #情况1：
            if nums[m] > nums[l]:
                if target >= nums[l] and target < nums[m]:
                    #递归左边
                    return dfs(l,m-1)
                else:
                    #递归右边
                    return dfs(m+1,r)
            #情况2
            if nums[m] < nums[l]:
                if target > nums[m] and target <= nums[r]:
                    #递归右边
                    return dfs(m+1,r)
                else:
                    #递归左边
                    return dfs(l,m-1)
        return dfs(0,len(nums)-1)
