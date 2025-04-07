class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Lead : OOB
        """
        n = len(nums)
        s = (n*(n+1))//2

        s2 = sum(nums)
        m = s -s2
        return m