class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()
        def dfs(x, y, l):
            if (x,y) in visited or l >= len(word):
                return False

            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False

            if board[x][y] != word[l]:
                return False

            # if we got to the last letter
            if l == len(word) - 1:
                return True 

            # if within range and board[x][y] == word[l]
            visited.add((x,y))
            for d in dirs:
                new_x = x + d[0]
                new_y = y + d[1]
                if dfs(new_x, new_y, l+1):
                    return True
            visited.remove((x,y))
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False