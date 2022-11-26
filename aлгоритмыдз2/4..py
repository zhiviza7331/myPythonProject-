#4
def maximumProfit(prices):
    m_p = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            m_p += prices[i] - prices[i - 1]
    return m_p
print(maximumProfit([7, 1, 5, 3, 6, 4]))