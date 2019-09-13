def coin_change(coins, amount):
    # init the dp table
    tab = [0 for _ in range(amount+1)]
    tab[0] = 1

    for j in range(len(coins)):
        for i in range(amount+1):
            if coins[j] <= i:
                tab[i] = tab[i-coins[j]] + tab[i]
    return tab[amount]


coins = [1, 2, 3, 8]  # coin denominations
amount = 3  # amount of money

print("No. of ways to change = {}".format(coin_change(coins, amount)))
