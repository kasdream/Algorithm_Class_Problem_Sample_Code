class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_product = []
        n = len(nums)
        
        #计算左积数组
        last_product = 1
        for i in range(n):
            left_product.append(nums[i]*last_product)
            last_product *= nums[i]
        
        #反向遍历，last_product维护右积数组结果
        last_product = 1
        for i in range(n-1,0,-1):
            left_product[i] = last_product * left_product[i-1]
            last_product *= nums[i]
        
        left_product[0] = last_product
        return left_product
            
