from collections import Counter
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = Counter(digits)
        result = 0
        for num in range(100, 1000, 2):
            d1, d2, d3 = num // 100, (num // 10) % 10, num % 10
            need = Counter([d1, d2, d3])
            if all(count[d] >= need[d] for d in need):
                result += 1
        return result
            