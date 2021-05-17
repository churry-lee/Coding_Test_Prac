# 리트코드 121
# 주식을 사고팔기 가장 좋은 시점
# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.

prices = [7, 1, 5, 3, 6, 4]     # return 5

def maxProfit(prices):
    min_price = prices[0]
    profit = 0

    for price in prices:
        # 최소값 갱신
        min_price = min(min_price, price)
        # 현재의 profit과 갱신된 금액의 차이 중 더 큰 값을 return
        profit = max(profit, price - min_price)
        print('min_price: {}, price: {}, profit: {}'.format(min_price, price, profit))

    return profit

print(maxProfit(prices))
