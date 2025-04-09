class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :lead OOB
        """
        seen = set()
        for i , x in reversed(list(enumerate(nums))):
            if x in seen:
                return (i+1+2)//3
            seen.add(x)
        return 0
