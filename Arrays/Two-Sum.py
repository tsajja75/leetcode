class Solution(object):
    def twoSum(self, nums, target):
        \\\
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        \\\
        ## map approch failed in case of duplicates
        # m = {}
        # for i in range(len(nums)):
        #     if i not in m:
        #          m[target-nums[i]]= i


        # for k,v in m.items():
        #     print(k,v)
        #     if k in nums:
        #         return [v,nums.index(k)]


        ## two pass hashmap

        # m ={}
        # for i in range(len(nums)):
        #     m[nums[i]] = i
        # for i in range(len(nums)):
        #     c = target-nums[i]
        #     if c in m and m[c]!=i:
        #         return [i, m[c]]
        # return[]

        ## onepass hashmap
        m ={}
        for i in range(len(nums)):
            c = target-nums[i]
            if c in m:
                return [i,m[c]]
            m[nums[i]]=i
        return []
