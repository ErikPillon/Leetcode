class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum())
        for ind,elem in enumerate(s.lower()):
            if not elem == s.lower()[-1-ind]:
                return False
        return True