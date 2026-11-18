
class Solution(object):
    def findSafeWalk(self, grid, health):
        from collections import deque

        m = len(grid)
        n = len(grid[0])

        q = deque()
        q.append((0, 0, health - grid[0][0]))

        if q[0][2] < 1:
            return False

        visited = [[0] * n for _ in range(m)]
        visited[0][0] = health - grid[0][0]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c, h = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_health = h - grid[nr][nc]

                    if new_health >= 1 and new_health > visited[nr][nc]:
                        visited[nr][nc] = new_health
                        q.append((nr, nc, new_health))

        return False
