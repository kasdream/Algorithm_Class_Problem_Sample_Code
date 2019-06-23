class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def dfs(nums,k):
            #一个数的时候，直接返回
            if len(nums) == 1: return nums[0]
            #取参照数
            x = nums[0]
            #定义左右区间
            i = 1; j = len(nums)-1
            #循环执行交换过程
            while ( i < j ):
                while ( i < j and nums[i] <= x ): i += 1
                while ( i < j and nums[j] >= x ): j -= 1
                if i == j: break
                nums[i],nums[j] = nums[j],nums[i]
                
            #退出的时候，判断nums[i]和x的关系，来决定如何交换
            if nums[i] <= x:
                nums[0],nums[i] = nums[i],nums[0]
            else:
                nums[0],nums[i-1] = nums[i-1],nums[0]
                i -= 1
            #根据i的位置来决定递归方向
            if i == k-1: return nums[i]
            elif k > i:
                return dfs(nums[i+1:],k-i-1)
            else:
                return dfs(nums[:i],k)
            
        #第K小就是第len-K+1大
        k = len(nums) - k + 1
        return dfs(nums,k)
            
