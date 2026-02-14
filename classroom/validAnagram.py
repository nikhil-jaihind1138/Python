class Solution:
    def isAnagram(self, s, t):
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        countT = {}
        countS = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countS.get(c, 0):
                return False
        return True


obj = Solution()
s = "anagram"
t = "nagamar"
r = obj.isAnagram(s, t)
print(r)
