class Solution(object):
    def topKFrequent(self, nums, k):
        \\\
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        \\\
        freq={}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        print(freq)
        sorted_elements = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_elements[:k]]