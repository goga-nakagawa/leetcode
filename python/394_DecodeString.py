class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def help(s):
            p, q = 0, len(s)-1
            while s[p] != '[':
                p += 1
            while s[q] != ']':
                q -= 1
            return s[p+1:q] * int(s[:p])

        return help(s)

# test 
s  = Solution()
print s.decodeString("3[a]2[bc]")
# assert s.decodeString("3[a]2[bc]") == "aaabcbc"
# assert s.decodeString("3[a2[c]]") == "accaccacc"
# assert s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"