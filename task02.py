import timeit

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
result = find_min_coins(113)
print(result)
result = find_min_coins(5003)
print(result)
result = find_min_coins(150958)
print(result)

print("Calculation of time used by find_coins_greedy")
print(timeit.timeit(lambda: find_min_coins(113), number=10))
print(timeit.timeit(lambda: find_min_coins(5003), number=10))
print(timeit.timeit(lambda: find_min_coins(150958), number=10))


#{1: 1, 2: 1, 10: 1, 50: 2}
#{1: 1, 2: 1, 50: 100}
#{1: 1, 2: 1, 5: 1, 50: 3019}
#Calculation of time used by find_coins_greedy
#0.0014816929997323314
#0.06571091799924034
#2.9394993980004074
