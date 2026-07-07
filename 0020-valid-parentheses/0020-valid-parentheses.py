class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', ']':'[', '}':'{'}
        l = []
        for i in s:
            if i in '([{':
                l.append(i)
            elif i in ')}]':
                if not l:  return False
                val = l.pop()
                if val != d[i]:return False
        return len(l) == 0
        