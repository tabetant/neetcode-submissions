class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        phone = {}
        phone['2'] = ["a", "b", "c"]
        phone['3'] = ["d", "e", "f"]
        phone['4'] = ['g', 'h', 'i']
        phone['5'] = ['j', 'k', 'l']
        phone['6'] = ['m', 'n', 'o']
        phone['7'] = ['p', 'q', 'r', 's']
        phone['8'] = ['t', 'u', 'v']
        phone['9'] = ['w', 'x', 'y', 'z']

        candidates = []
        result = []
        for d in digits:
            candidates.append(phone[d])

        def backtrack(current):
            if len(current) == len(candidates):
                result.append(current)
                return

            for c in candidates[len(current)]:
                current += c
                backtrack(current)
                current = current[:len(current) - 1]
            
        backtrack("")
        return result


    