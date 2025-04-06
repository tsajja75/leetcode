class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt=0
        for i in range(1, len(nums)):
            if nums[i]<nums[i-1]:
                cnt+=1

        print(cnt)
        if nums[len(nums)-1]>nums[0]:
            cnt+=1
        print(cnt)
        return cnt<=1
        