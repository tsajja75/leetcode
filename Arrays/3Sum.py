class Solution(object):
    def threeSum(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[List[int]]
        \\\

        ## brute force 
        # res =[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if i!=j and i!=k and j!=k:
        #                if  nums[i] + nums[j] + nums[k] == 0:
        #                 v=sorted([nums[i], nums[j],nums[k]])
        #                 if v not in res:
        #                     res.append(v)
        # return res

        # two pointer
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res
        