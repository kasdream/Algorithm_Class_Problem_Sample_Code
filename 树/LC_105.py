# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        #边界条件
        if len(preorder) == 0: return None
        
        #记录中序每个值的下标
        d = {}
        for i,val in enumerate(inorder):
            d[val] = i
        
        def dfs(lpre,rpre,lin,rin):
            #边界条件
            if lpre > rpre: return None
            if lpre == rpre:
                return TreeNode(preorder[lpre])
            
            #前序的第一个值是根节点
            root = TreeNode(preorder[lpre])
            #取出中序的根节点
            idx = d[root.val]
            
            #递归左右子树
            left_tree = dfs(lpre+1,lpre+(idx-lin),lin,idx-1)
            right_tree = dfs(lpre+(idx-lin)+1,rpre,idx+1,rin)
            
            #连回根节点
            root.left = left_tree
            root.right = right_tree
            #返回
            return root
        return dfs(0,len(preorder)-1,0,len(inorder)-1)
