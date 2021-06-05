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

    def closestValue(self, root, target):
        # 二叉搜索树中最接近目标的节点值
        res = root.val
        while root:
            diff1 = abs(res - target)
            diff2 = abs(root.val - target)
            if diff2 < diff1:
                res = root.val
            root = root.left if target < root.val else root.right
        return res

    def levelOrder(self, root):
        """
        二叉树层序遍历
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            r = queue.pop(0)
            res.append(r.val)
            if r.left:
                queue.append(r.left)
            if r.right:
                queue.append(r.right)
        return res

    def isSubStructure(self, A, B):
        """
        判断树B是否树A的子结构
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """

        def hasTree(root1, root2):
            if not root2:
                return True
            if not root1:
                return False
            if root1.val != root2.val:
                return False
            return hasTree(root1.left, root2.left) and hasTree(root1.right, root2.right)

        if A and B:
            if hasTree(A, B):
                return True
            return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
        return False