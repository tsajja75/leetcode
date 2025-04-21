class Solution(object):
    def maxProfit(self, prices):
        \\\
        :type prices: List[int]
        :rtype: int
        \\\
        sp = 0
        buy=0
        sell = 1

        while buy<sell and sell<len(prices):
            transaction = prices[sell]-prices[buy]
            sp=max(sp,transaction)
            if prices[buy]>prices[sell]:
                buy=sell
            sell+=1
        return(sp)
        