class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap: dict[Tuple[int, ...], List[str]] = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord('a') - ord(c)] += 1
            key = tuple(count)
            if key not in anagramMap:
                anagramMap[key] = []
            anagramMap[key].append(s)
        return list(anagramMap.values())