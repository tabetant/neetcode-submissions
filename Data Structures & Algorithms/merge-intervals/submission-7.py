class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda i: i[0])
        result = []
        for i in intervals:
            if len(result) == 0:
                result.append(i)
                continue
            prev = result[-1]
            if i[0] <= prev[1]:
                result.pop()
                prev[1] = max(prev[1], i[1])
                result.append(prev)
            else:
                result.append(i)
        return result


