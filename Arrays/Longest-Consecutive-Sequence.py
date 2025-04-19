class Solution(object):
    def longestConsecutive(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\

        

        nums = set(nums)
        log =0
        for n in nums:
            if n-1 not in nums:
                length =1
                while n + length in nums:
                    length +=1
                log = max(log,length)
        return log