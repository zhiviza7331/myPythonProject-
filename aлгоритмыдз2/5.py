#5
def getDescentPeriods(prices):
    a = len(prices)
    dp = [0] * a
    dp[0] = 1
    for i in range(1, a):
        dp[i] = 1
        if prices[i] == prices[i - 1] - 1:
            dp[i] += dp[i - 1]
    return sum(dp)
print(getDescentPeriods([3, 2, 1 ,4]))