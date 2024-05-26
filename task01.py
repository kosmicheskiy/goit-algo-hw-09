import timeit

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
result = find_coins_greedy(113)
print(result)
result = find_coins_greedy(5003)
print(result)
result = find_coins_greedy(150958)
print(result)

print("Calculation of time used by find_coins_greedy")
print(timeit.timeit(lambda: find_coins_greedy(113), number=10))
print(timeit.timeit(lambda: find_coins_greedy(5003), number=10))
print(timeit.timeit(lambda: find_coins_greedy(150958), number=10))


#{50: 2, 10: 1, 2: 1, 1: 1}
#{50: 100, 2: 1, 1: 1}
#{50: 3019, 5: 1, 2: 1, 1: 1}
#Calculation of time used by find_coins_greedy
#1.2884000170743093e-05
#1.0990999726345763e-05
#1.2559999959194101e-05
