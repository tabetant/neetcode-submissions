class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque([])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        for x in range (len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    fresh += 1
                elif grid[x][y] == 2:
                    q.append((x,y))
        if fresh == 0: return 0
        minutes = 0
        while q:
            level_size = len(q)
            for _ in range (level_size):
                n = q.popleft()
                for d in directions:
                    newx = n[0] + d[0]
                    newy = n[1] + d[1]
                    if newx < 0 or newy < 0 or newx >= len(grid) or newy >= len(grid[0]):
                        continue
                    elif grid[newx][newy] == 1:
                        grid[newx][newy] = 2
                        fresh -= 1
                        q.append((newx, newy))
            minutes += 1
            if fresh == 0:
                break
        return minutes if fresh == 0 else -1