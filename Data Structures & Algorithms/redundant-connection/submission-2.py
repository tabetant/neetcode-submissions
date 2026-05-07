class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x,y):
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[px] = py
            return True
        for e in edges:
            if not union(e[0], e[1]):
                return e
        return []