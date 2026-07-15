class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        small = s.lower()
        i, j = 0, n - 1
        while i < j:
            if not small[i].isalnum():
                i += 1
                continue
            if not small[j].isalnum():
                j -= 1
                continue
            if small[i] != small[j]:
                return False
            i += 1
            j -= 1
        return True
            