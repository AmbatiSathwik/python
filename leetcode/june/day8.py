# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preindex = 0
        def tree(preorder, inorder, start, end,arr):
            if start > end:
                return None
            root = TreeNode(preorder[self.preindex])
            self.preindex += 1
            
            if start == end:
                return root
            k = arr[root.val]
            #print(k)
            root.left = tree(preorder,inorder,start,k-1,arr)
            root.right = tree(preorder,inorder,k+1, end,arr)
            return root
        def hashing(pre, inn, n):
            arr = {}
            for i in range(n):
                arr[inn[i]] = i
            return tree(pre,inn,0,n-1,arr)
        self.preindex = 0
        root = hashing(preorder,inorder,len(inorder))
        return root
