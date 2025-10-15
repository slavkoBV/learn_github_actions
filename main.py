
def exchange_coins(cash: int) -> dict:
    coins = {}
    for i in (50, 25, 10, 5, 2, 1):
        res = cash // i
        if res:
            coins[i] = res
        cash %= i
    return coins
if __name__ == '__main__':
    initial_cash = 1000
    result = exchange_coins(initial_cash)
    print(result)
