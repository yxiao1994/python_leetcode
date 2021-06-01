class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        temp = []

        def dfs(root, target):
            if not root:
                return
            temp.append(root.val)
            if root.val == target and not root.left and not root.right:
                res.append(temp[:])
            dfs(root.left, target - root.val)
            dfs(root.right, target - root.val)
            temp.pop()

        dfs(root, target)
        return res
