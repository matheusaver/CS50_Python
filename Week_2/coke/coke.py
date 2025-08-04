CONST_COKE_PRICE = 50

def main():
    total = 0
    while total < CONST_COKE_PRICE:
        print(f"Amount due: {CONST_COKE_PRICE - total}")
        user_input = int(input("Insert coin: "))
        total += valide_coin(user_input)
    print(f"Change owed: {total - CONST_COKE_PRICE}")


def valide_coin(coin):
        if coin == 25 or coin == 10 or coin == 5:
            return coin
        else:
            return 0

if __name__ == "__main__":
    main()
