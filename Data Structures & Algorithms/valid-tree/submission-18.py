class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        state = [0] * n
        adj = defaultdict(list)
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        visited = set()
        
        def dfs(node, parent):
            visited.add(node)
            for a in adj[node]:
                if a == parent:
                    continue
                if a in visited:
                    return False
                if not dfs(a, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n