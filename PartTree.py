from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    def _BuildTree(self, preorder, inorder, Pre_left, Pre_right, In_left, In_right):
        if len(preorder) == 0:
            return None
        if Pre_left > Pre_right or In_left > In_right:
            return None
        left_tree_len = 0
        In_index = In_left
        while In_index < In_right and inorder[In_index] != preorder[Pre_left]:
            In_index += 1
            left_tree_len += 1

        root = TreeNode(preorder[Pre_left])
        root.left = self._BuildTree(preorder, inorder, Pre_left + 1, Pre_left + left_tree_len, In_left, In_index - 1)
        root.right = self._BuildTree(preorder, inorder, Pre_left + left_tree_len + 1, Pre_right, In_index + 1, In_right)
        return root

    def buildTree(self, preorder, inorder):
        """
        从前序与中序遍历序列构造二叉树
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        return self._BuildTree(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)

    def pathSum(self, root, target):
        """
        和为某一值的路径
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

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        queue = [root]
        flag = True
        while queue:
            temp_num = len(queue)
            temp = deque([])
            for _ in range(temp_num):
                node = queue.pop(0)
                if flag:
                    temp.append(node.val)
                else:
                    temp.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(temp))
            flag = not flag
        return res

    def generateTrees(self, n):
        """
        生成并返回所有由 n 个节点组成且节点值从 1 到 n
        互不相同的不同 二叉搜索树
        :type n: int
        :rtype: List[TreeNode]
        """

        def generateBST(min_val, max_val):
            if min_val > max_val:
                return [None]
            res = []
            for root_val in range(min_val, max_val + 1):
                for left_tree in generateBST(min_val, root_val - 1):
                    for right_tree in generateBST(root_val + 1, max_val):
                        root = TreeNode(root_val)
                        root.left = left_tree
                        root.right = right_tree
                        res.append(root)
            return res

        return generateBST(1, n) if n else []

    def isValidBST(self, root):
        """
        判断是否是二叉搜索树
        :type root: TreeNode
        :rtype: bool
        """

        def helper(root, lower=float('-inf'), upper=float('inf')):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)

        return helper(root)

    def rightSideView(self, root):
        """
        二叉树的右视图
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            qsize = len(queue)
            res.append(queue[-1].val)
            for _ in range(qsize):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
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

    def isSymmetric(self, root):
        """
        是否镜像树
        :param root:
        :return:
        """

        def isReverse(A, B):
            if not A and not B:
                return True
            if A and B:
                if A.val != B.val:
                    return False
                return isReverse(A.left, B.right) and isReverse(A.right, B.left)
            return False

        return isReverse(root.left, root.right) if root else True

    def binaryTreePaths(self, root):
        # write your code here
        # 从根节点到叶子节点的所有路径
        res = []
        temp = []

        def dfs(root):
            if not root:
                return
            temp.append(str(root.val))
            if not root.left and not root.right:
                res.append(temp[:])
            dfs(root.left)
            dfs(root.right)
            temp.pop()

        dfs(root)
        return ['->'.join(x) for x in res]

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        res.append(float('-inf'))

        def pathSum(root):
            if not root:
                return 0
            left_val = pathSum(root.left)
            right_val = pathSum(root.right)
            curr = root.val + max(left_val, 0) + max(right_val, 0)
            if curr > res[0]:
                res[0] = curr
            return root.val + max(left_val, right_val, 0)

        pathSum(root)
        return res[0]


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def help_deseralize(self, l):
        if not l:
            return None
        x = l.pop(0)
        root = None
        if x != '#':
            root = TreeNode(int(x))
            root.left = self.help_deseralize(l)
            root.right = self.help_deseralize(l)
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.help_deseralize(data.split(','))
