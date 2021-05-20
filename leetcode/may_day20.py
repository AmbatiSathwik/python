# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root is None:
            return 0
        else :
            lDepth = self.height(root.left)
            rDepth = self.height(root.right)
            return lDepth+1 if lDepth > rDepth else rDepth + 1
    def solve(self,root,li,level):
        if root is None:
            return
        else:
            li[level].append(root.val)
            self.solve(root.left,li,level+1)
            self.solve(root.right,li,level+1)
        return
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        k = self.height(root)
        li = [[] for i in range(k)]
        self.solve(root,li,0)
        print(li)
        return li
