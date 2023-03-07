'''
Sliding Window

EASY
1. Best Time to Buy and Sell Stock:

# QUESTION:

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

# SOLUTION

two pointers:
start of w the pointers side by side
setmax profit to 0, initially, so if theres only loss, we'll return 0
record their difference, and move on
if at some point the right side value is smaller than the left, left = right, and right =+ 1

 

'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left, right = 0, 1
        maxProfit = 0 #so if there are no profits, it returns 0 

        while right < len(prices):

            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit) #records max difference, and checks w the current profit
            else:
                left = right #left should always be the smallest value
            right += 1
        return maxProfit
        

