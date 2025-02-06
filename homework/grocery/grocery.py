def main():
    products = {}
    while True:
        try:
            item = input().strip().upper()
            if item not in products.keys():
                products[item] = 1
            else:
                products[item] += 1
        except EOFError:
            # sort the list
            for key in sorted(products.keys()):  # Sort alphabetically
                print(f"{products[key]} {key}")  # Print count and item
            break

if __name__ == "__main__":
    main()
