class Solution(object):
    def containsDuplicate(self, nums):
        \\\
        :type nums: List[int]
        :rtype: bool
        \\\


        # ## Brute Force did not workout in all the cases
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         print(nums[j:len(nums)])
        #         if i in nums[j+1:]:
        #             return True
        # return False


        # idea 2:  Best one 
        if len(nums) == len(set(nums)):
            return False
        else:
            return True


        #approch 2 time limit exeded
        # res = []  
        # for i in nums:
        #     if i not in res:
        #         res.append(i)
        #     else:
        #         return True
        # return False


        ## Hashmap approch
        # m = {}
        # for i in nums:
        #     if i not in m:
        #         m[i]=1
        #     else:
        #         return True
        # return False

        ## approch 3  sorting:
        ## wrong done using selection sort need to do with quick sort
        # for i in range(0,len(nums)-1):
        #     mini = i
        #     for j in range(i+1,len(nums)):
        #         if nums[j]<nums[mini]:
        #             mini=j
        #         elif nums[j] == nums[mini]:
        #             return True
        #         else: 
        #             pass
        #     nums[i],nums[mini]= nums[mini],nums[i]
        # print(nums)
        # return False
                








        