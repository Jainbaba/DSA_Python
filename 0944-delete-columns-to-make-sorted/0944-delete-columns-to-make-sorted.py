class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum([1 for s in zip(*strs) if list(s) != sorted(s)])