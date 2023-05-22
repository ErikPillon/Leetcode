class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {*s}
        s2 = dict([(i,0) for i in s1])
        t1 = {*t}
        t2 = dict([(i,0) for i in t1])
        for i in s:
            s2[i] += 1
        for i in t:
            t2[i] += 1
        return t2 == s2