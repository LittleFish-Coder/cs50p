amount = 50

while amount > 0:
    print(f"Amount Due: {amount}")
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        amount = amount - coin
    else:
        pass

amount = amount * -1
print(f"Change Owed: {amount}")


