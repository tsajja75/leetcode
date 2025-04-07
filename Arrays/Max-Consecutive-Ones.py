class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=0
        l=0
        for i in range(len(nums)):
            if nums[i] ==1:
                m+=1
            else:
                m=0
            l= max(l,m)
        return l
        
        