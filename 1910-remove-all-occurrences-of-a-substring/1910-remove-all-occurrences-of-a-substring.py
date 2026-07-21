class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        l = []
        n = len(part)
        for ch in s:
            l.append(ch)
            if len(l) >= n and ''.join(l[-n:]) == part:
                del l[-n:]
        return ''.join(l)