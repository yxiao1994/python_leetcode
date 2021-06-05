class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def check(i, j, k, word, m, n, visited):
            if k == len(word) - 1:
                return board[i][j] == word[k]
            if board[i][j] != word[k]:
                return False
            visited[i][j] = True
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    if check(x, y, k + 1, word, m, n, visited):
                        return True
            visited[i][j] = False
            return False

        for i in range(m):
            for j in range(n):
                if check(i, j, 0, word, m, n, visited):
                    return True
        return False

    def permutation(self, s):
        """
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

if __name__ == "__main__":
    obj = Solution()
    print(obj.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                    "ABCCED"))
