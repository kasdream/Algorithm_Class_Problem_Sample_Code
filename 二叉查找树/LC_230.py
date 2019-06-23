# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#定义全局变量cnt
global cnt
class Solution(object):
    def dfs(self,root):
        global cnt
        #边界条件，如果root为空，返回-1
        if root is None: return -1
        
        #先递归左边，记录返回结果
        res = self.dfs(root.left)
        #如果递归完发现cnt减到0了，那么返回结果
        if cnt == 0: return res
        
        #否则cnt-1，如果到0了，那么当前节点就是第k小节点
        cnt -= 1
        if cnt == 0: return root.val
        
        #其他情况肯定在右子树上，直接返回递归右边的结果
        return self.dfs(root.right)
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #cnt赋值为k
        global cnt
        cnt = k
        return self.dfs(root)
            
