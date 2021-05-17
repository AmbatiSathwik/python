class Solution:
    camera = 0
    def check(self,root):
        if root is None:
            return 0
        val = self.check(root.left) + self.check(root.right)
        if val == 0: #0 only if it is leaf so no monitering is need to pass
            return 3
        if val < 3: #children cotaining camera so no monetering requires
            return 0
        self.camera += 1 #their children is not monitering so need to moniter
        return 1
            
            
        
    def minCameraCover(self, root: TreeNode) -> int:
        if self.check(root) > 2:
            return self.camera + 1
        else:
            return self.camera
