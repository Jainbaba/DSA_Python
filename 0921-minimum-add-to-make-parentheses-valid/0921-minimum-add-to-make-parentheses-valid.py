class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        while(s.find("()") != -1):
            s = s.replace("()","")
        return len(s)
        