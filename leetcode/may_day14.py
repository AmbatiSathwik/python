class Solution:
    def maxi(self,node):
        if node.right is not None:
            return self.maxi(node.right)
        return node
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        elif root.left is not None:
            left_max = self.maxi(root.left)
            left_max.right = root.right
            root.right = root.left
            root.left = None
        self.flatten(root.right)
