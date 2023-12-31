class Solution(object):
    def backspaceCompare(self, s, t):
        s1, t1 = '', ''

        i = 0
        while i != len(s):
            if s[i] == '#':
                s1 = s1[:-1]
            else:
                s1 += s[i]
            i += 1

        i = 0
        while i != len(t):
            if t[i] == '#':
                t1 = t1[:-1]
            else:
                t1 += t[i]
            i += 1

        return s1 == t1

res = Solution().backspaceCompare("xywrrmp", "xywrrm#p")
print(res)