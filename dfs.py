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


if __name__ == "__main__":
    obj = Solution()
    print(obj.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
    "ABCCED"))