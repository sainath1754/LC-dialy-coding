from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for stng in strs:
            counts = [0]*26
            for i in stng:
                counts[ord(i)-ord('a')]+=1
            result[tuple(counts)].append(stng)
        return list(result.values())
        