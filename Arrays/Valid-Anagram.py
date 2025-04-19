class Solution(object):
    def isAnagram(self, s, t):
        \\\
        :type s: str
        :type t: str
        :rtype: bool
        \\\
        m={}
        n={}


        for i in s:
            if i not in m:
                m[i]=1
            else :
                m[i]+=1
   
        for j in t:
            if j not in n:
                n[j]=1
            else:
                n[j]+=1
                
        return m==n

        
        