class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for n in adj[node]:
                dfs(n)
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
        