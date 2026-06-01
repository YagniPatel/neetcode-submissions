class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        # Approach 1: Recursion

        # directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        # rows, cols = len(matrix), len(matrix[0])

        # def dfs(r, c, pre):
        #     if 0 > r or r >= rows or 0 > c or c >= cols or matrix[r][c] <= pre:
        #         return 0
            
        #     res = 1
        #     for dr, dc in directions:
        #         res = max(res, 1 + dfs(r+dr, c+dc, matrix[r][c]))

        #     return res

        # res = 0
        # for r in range(rows):
        #     for c in range(cols):
        #         res = max(res, dfs(r, c, float("-inf")))
        
        # return res


        # Approach 2: Dynamic Programming (Top - Down)

        # directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        # rows, cols = len(matrix), len(matrix[0])
        # dp = {}

        # def dfs(r, c, pre):
        #     if min(r, c) < 0 or r >= rows or c >= cols or matrix[r][c] <= pre:
        #         return 0
        #     if (r, c) in dp:
        #         return dp[(r, c)]

        #     res = 1
        #     for dr, dc in directions:
        #         res = max(res, 1 + dfs(r + dr, c + dc, matrix[r][c]))

        #     dp[(r, c)] = res
        #     return res

        # for r in range(rows):
        #     for c in range(cols):
        #        dfs(r, c, -1)

        # return max(dp.values())


        # Approach 3: Topological Sort (Kahn's Algorithm)

        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        rows, cols = len(matrix), len(matrix[0])
        ind = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if min(nr, nc) < 0 or nr >= rows or nc >= cols or matrix[nr][nc] >= matrix[r][c]:
                        continue
                    ind[r][c] += 1

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if ind[r][c] == 0:
                    q.append((r,c))

        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr >= rows or nc >= cols or matrix[nr][nc] <= matrix[r][c]:
                        continue

                    ind[nr][nc] -= 1
                    if ind[nr][nc] == 0:
                        q.append((nr, nc))

        return res