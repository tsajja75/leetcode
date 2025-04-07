class Solution(object):
    def sortColors(self, arr):
        \\\
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        Lead Insertion Sort
        \\\

        for i in range(0,len(arr)-1):
            mini= i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[mini]:
                    mini=j
            arr[mini],arr[i] = arr[i],arr[mini]