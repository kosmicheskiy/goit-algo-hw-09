def find_coins_greedy(amount):
    denominations = [50, 20, 10, 5, 2, 1]  # доступні номінали монет
    coins_used = {}  # словник для зберігання кількості монет кожного номіналу

    for coin in denominations:
        if amount >= coin:
            num_coins = amount // coin
            coins_used[coin] = num_coins
            amount -= num_coins * coin

    return coins_used

# Приклад використання
amount = 113
result = find_coins_greedy(amount)
print(result)
#{50: 2, 10: 1, 2: 1, 1: 1}
