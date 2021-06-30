# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        l = []
        def path(root,p):
            if root == None:
                return False
            if root == p:
                return True
            a = path(root.left,p)
            if a:
                l.append(root.val) 
                return True
            
            b = path(root.right,p)
            if b:
                l.append(root.val)
                return True
            return False
        a = b =[]
        
        path(root,p)
        a = l[:]
        a.insert(0,p.val)
        l = []
        path(root,q)
        b = l[:]
        b.insert(0,q.val)
        lst3 = [value for value in a if value in b]
        return(TreeNode(lst3[0]))
