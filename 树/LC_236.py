# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #边界条件
        if root is None: return None
        #如果root是pq之一，返回root
        if root == p or root == q: return root
        
        #递归左右两边
        res1 = self.lowestCommonAncestor(root.left,p,q)
        res2 = self.lowestCommonAncestor(root.right,p,q)
        
        #返回结果
        if res1 is None: return res2
        if res2 is None: return res1
        return root
