class Solution(object):
    def groupAnagrams(self, strs):
        d = {}

        for _ in strs:
            key = tuple(sorted(_))

            if key in d:
                d[key].append(_)
            else:
                d[key] = [_]

        return list(d.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
obj = Solution()
r = obj.groupAnagrams(strs)
print(r)