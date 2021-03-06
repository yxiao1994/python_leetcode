class Solution(object):
    def exist(self, board, word):
        """
        矩阵中的路径
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def check(i, j, k):
            if k == len(word) - 1:
                return board[i][j] == word[-1]
            if board[i][j] != word[k]:
                return False
            visited[i][j] = True
            directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    if check(x, y, k + 1):
                        return True
            visited[i][j] = False
            return False

        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
                    return True
        return False

    def longestIncreasingPath(self, matrix):
        """
        矩阵中的最长递增路径长度
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1))

        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            max_path = 1
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and matrix[i][j] > matrix[x][y]:
                    max_path = max(max_path, dfs(x, y) + 1)
            dp[i][j] = max_path
            return max_path

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res

    def permutation(self, s):
        """
        字符串的排列
        :type s: str
        :rtype: List[str]
        """
        res = []
        temp = list(s)

        def dfs(start, n):
            if start == n:
                res.append(temp[:])
                return
            for i in range(start, n):
                temp[start], temp[i] = temp[i], temp[start]
                dfs(start + 1, n)
                temp[start], temp[i] = temp[i], temp[start]

        dfs(0, len(temp))
        return list(set([''.join(x) for x in res]))

    def combine(self, n, k):
        """
        k个数的组合
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        if n <= 0:
            return res

        def dfs(start):
            if len(temp) == k:
                res.append(temp[:])
            for i in range(start, n + 1):
                temp.append(i)
                dfs(i + 1)
                temp.pop()

        dfs(1)
        return res

    def subsets(self, nums):
        """
        数组的子集
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        n = len(nums)
        if n <= 0:
            return res

        def dfs(start):
            if start == n:
                res.append(temp[:])
                return
            dfs(start + 1)
            temp.append(nums[start])
            dfs(start + 1)
            temp.pop()

        dfs(0)
        return res

    def subsetsWithDup(self, nums):
        """
        包含重复元素的子集
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        if n == 0:
            return res
        nums = sorted(nums)
        temp = []

        def dfs(choosePre, start):
            if start == n:
                res.append(temp[:])
                return
            dfs(False, start + 1)
            if not choosePre and start >= 1 and nums[start] == nums[start - 1]:
                return
            temp.append(nums[start])
            dfs(True, start + 1)
            temp.pop()

        dfs(False, 0)
        return res

    def generateParenthesis(self, n):
        """
        括号生成
        :type n: int
        :rtype: List[str]
        """
        temp = []
        res = []

        def dfs(left, right):
            if len(temp) == 2 * n:
                res.append(''.join(temp[:]))
                return
            if left < n:
                temp.append('(')
                dfs(left + 1, right)
                temp.pop()
            if right < n and right < left:
                temp.append(')')
                dfs(left, right + 1)
                temp.pop()

        dfs(0, 0)
        return res

    def numIslands(self, grid):
        # 岛屿个数
        def dfs(grid, x, y, m, n):
            grid[x][y] = 0
            directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
            for dx, dy in directions:
                x_new = x + dx
                y_new = y + dy
                if 0 <= x_new < m and 0 <= y_new < n and grid[x_new][y_new] == 1:
                    dfs(grid, x_new, y_new, m, n)

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1
                    dfs(grid, i, j, m, n)
        return res

    def numDistinctIslands(self, grid):
        """
        不同岛屿的数量
        :type grid: List[List[int]]
        :rtype: int
        """
        Row, Col = len(grid), len(grid[0])
        visited = [[False for _ in range(Col)] for _ in range(Row)]

        def dfs(r, c):
            if visited[r][c]:
                return
            visited[r][c] = 1

            nxt = [(r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)]
            for i in range(4):
                nr, nc = nxt[i]
                if 0 <= nr < Row and 0 <= nc < Col and grid[nr][nc] == 1:
                    self.path += str(i + 1)
                    dfs(nr, nc)

        rec = set()

        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == 1 and visited[r][c] == False:
                    self.path = "0"
                    dfs(r, c)
                    rec.add(self.path)

        return len(rec)

    def surrounded_region(self, board):
        """
        被围绕的区域
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])

        def dfs(i, j):
            if board[i][j] != 'O':
                return
            board[i][j] = '#'
            directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                    dfs(x, y)

        for j in range(0, n):
            dfs(0, j)
            dfs(m - 1, j)
        for i in range(1, m - 1):
            dfs(i, 0)
            dfs(i, n - 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'


if __name__ == "__main__":
    obj = Solution()
    print(obj.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                    "ABCCED"))
