class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = ''.join(x for x in s if x.isalnum())
        s_re = list(s)
        s_re.reverse()
        s_re = ''.join(s_re)
        return s == s_re