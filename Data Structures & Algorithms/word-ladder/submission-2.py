class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def diff_by_one(w1, w2):
            diff = 0
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    diff += 1
            return diff == 1

        q = deque([beginWord])
        steps = 1
        visited = set()
        visited.add(beginWord)
        while q:
            level_size = len(q)
            for _ in range(level_size):
                word = q.popleft()
                if word == endWord:
                    return steps
                for n in wordList:
                    if n not in visited and diff_by_one(word, n):
                        visited.add(n)
                        q.append(n)
            steps += 1
        return 0