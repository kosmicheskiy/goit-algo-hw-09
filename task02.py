def find_min_coins(amount):
    denominations = [1, 2, 5, 10, 20, 50]  # доступні номінали монет
    coins_used = [float('inf')] * (amount + 1)
    coins_used[0] = 0
    last_coin = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in denominations:
            if coin <= i and coins_used[i - coin] + 1 < coins_used[i]:
                coins_used[i] = coins_used[i - coin] + 1
                last_coin[i] = coin

    coins_count = {}
    remaining_amount = amount
    while remaining_amount > 0:
        coin = last_coin[remaining_amount]
        if coin in coins_count:
            coins_count[coin] += 1
        else:
            coins_count[coin] = 1
        remaining_amount -= coin

    return coins_count

# Приклад використання
amount = 113
result = find_min_coins(amount)
print(result)
#{1: 1, 2: 1, 10: 1, 50: 2}
