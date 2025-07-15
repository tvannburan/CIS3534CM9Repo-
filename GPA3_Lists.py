def getInfo():
    symbol = ["BTC", "ETH","USDT","BNB","USDC","ADA","SOL"]
    name = ["Bitcoin", "Ethereum","Tether","Binance Coin","USD Coin","Cardano","Solana"]
    price = [50000.0, 4000.0, 1.0, 300.0, 1.0, 20.0, 100.0]

    coins = [symbol]
    coins.append(name)
    coins.append(price)
    return coins

def main():
    coins = getInfo()
    symbol = coins[0]
    name = coins[1]
    price = coins[2]

    selected_names = []
    total = 0.0

    if len(coins) > 0:
        print("Here are the coins:")
        print("Symbol  Name   Price")
        print("-------------------------------")
        for i in range(0, len(symbol)):
            print(symbol[i], name[i], "$" + str(price[i]))

    while True:
        choice = input("Enter a coin symbol to select (or 'x' to finish): ").upper()
        if choice == 'X' or choice == 'x':
            break
        if choice in symbol:
            index = symbol.index(choice)
            selected_names.append(name[index])
            print("Selected:", name[index], "at price $"+str(price[index]))
            total += price[index]
        else:
            print("Coin not found.")

    print("Here are your purchased coins:")
    print(selected_names)
    print("The total value of your purchases is $" + str(total))

if __name__ == "__main__":
    main()


#changes for github