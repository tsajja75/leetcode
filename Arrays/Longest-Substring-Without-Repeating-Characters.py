class Solution(object):
    def lengthOfLongestSubstring(self, s):
        \\\
        :type s: str
        :rtype: int
        \\\
        
        l =m =0
        ch=set()

        for r in range(len(s)):
            while s[r] in ch:
                ch.remove(s[l])
                l+=1
            ch.add(s[r])
            m=max(m,r-l+1)
        return m