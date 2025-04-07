class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :lead: hashmap
        """
        m ={}


        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i]+=1
        for k,v in m.items():
            if v ==1:
                return k

        