class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        q = deque([])
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    q.append((x,y))
        distance = 1
        while q:
            level_size = len(q)
            for _ in range (level_size):
                n = q.popleft()
                for d in directions:
                    newx = n[0] + d[0]
                    newy = n[1] + d[1]
                    if newx < 0 or newy < 0 or newx >= len(grid) or newy >= len(grid[0]):
                        continue
                    elif grid[newx][newy] == INF:
                        grid[newx][newy] = distance
                        q.append((newx, newy))
            distance += 1 
        return None
        