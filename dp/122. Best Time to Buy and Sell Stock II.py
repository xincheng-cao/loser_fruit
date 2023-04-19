class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        not_hold_max_profit = [0] * len(prices)
        holding_max_profit = [0] * len(prices)

        holding_max_profit[0] = holding_max_profit[0] - prices[0]
        for i in range(1, len(prices)):
            not_hold_max_profit[i] = max(
                # from prev not hold 2 not hold
                not_hold_max_profit[i - 1],
                # from prev hold 2 not hold
                holding_max_profit[i - 1] + prices[i],
            )
            holding_max_profit[i] = max(
                # from prev not hold 2 hold
                not_hold_max_profit[i - 1] - prices[i],
                # from prev hold 2 hold
                holding_max_profit[i - 1] + prices[i] - prices[i],  # which is holding_max_profit[i-1]

            )
        return not_hold_max_profit[-1]





