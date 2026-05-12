class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            for c in s:
                encoded += chr((ord(c) - 10))
            encoded += "#"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        string = ""
        for i in range(len(s)):
            if s[i] == "#":
                decoded.append(string)
                string = ""
            else:
                string += chr((ord(s[i]) + 10))
        print(s)
        return decoded