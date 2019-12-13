#O(n) solution 
#Input: [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.


def maxProfit(prices):
        mini = 999999999
        profit = 0
        for i in range(len(prices)):
            if prices[i]<mini:
                mini = prices[i]
            profit = max(profit,prices[i] - mini)
        return profit
