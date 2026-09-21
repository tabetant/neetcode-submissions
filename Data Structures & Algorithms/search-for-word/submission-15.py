class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        dirs = [(0,1), (0,-1), (-1,0), (1,0)]
        def dfs(x, y, curr_len):
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or curr_len >= len(word) or (x,y) in visited or board[x][y] != word[curr_len]:
                return False
            elif curr_len == len(word) - 1 and board[x][y] == word[curr_len]:
                return True

            
            visited.add((x,y))
            for d in dirs:
                if dfs(x+d[0], y+d[1], curr_len + 1):
                    return True
            visited.remove((x,y))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j, 0):
                    return True
        return False