class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        Lead: this soution is designed based on possible inversion (sorted array should only    
        have only one inversion) 
        """


        cnt=0
        for i in range(1, len(nums)):
            if nums[i]<nums[i-1]:
                cnt+=1
        if nums[len(nums)-1]>nums[0]:
            cnt+=1
        return cnt<=1
        