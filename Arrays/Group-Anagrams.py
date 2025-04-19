class Solution(object):
    def groupAnagrams(self, strs):
        \\\
        :type strs: List[str]
        :rtype: List[List[str]]
        \\\
        
        m = defaultdict(list)
        for i in strs:
            re= \\.join(sorted(i))
            m[re].append(i)
        return list(m.values())
    


        

        




        
        