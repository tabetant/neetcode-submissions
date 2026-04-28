class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = set()
        pacific = set()
        atlantic = set()

        def bfs(starts, visited):
            q = deque(starts)
            visited.update(starts)
            while q:
                level_size = len(q)
                for _ in range(level_size):
                    n = q.popleft()

                    visited.add(n)
                    for d in directions:
                        newx, newy = n[0] + d[0], n[1] + d[1]
                        if newx < 0 or newy < 0 or newx >= len(heights) or newy >= len(heights[0]) or (newx, newy) in visited:
                            continue
                        if heights[newx][newy] >= heights[n[0]][n[1]]:
                            visited.add((newx, newy))
                            q.append((newx, newy))

        
        pacific_starts = [(r,0) for r in range (len(heights))] + [(0,c) for c in range(len(heights[0]))]
        atlantic_starts = [(r, len(heights[0]) - 1) for r in range (len(heights))] + [(len(heights) - 1, c) for c in range(len(heights[0]))]

        bfs(pacific_starts, pacific)
        bfs(atlantic_starts, atlantic)
                    
        return [[r,c] for r in range(len(heights)) for c in range (len(heights[0])) if (r,c) in pacific and (r,c) in atlantic]
