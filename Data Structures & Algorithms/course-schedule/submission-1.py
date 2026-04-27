class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        state = [0] * numCourses
        prereqs = defaultdict(list)
        for p in prerequisites:
            prereqs[p[0]].append(p[1])
        def dfs(course):
            if state[course] == 1: return False
            if state[course] == 2: return True
            state[course] = 1
            for p in prereqs[course]:
                if not dfs(p): return False
            state[course] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True