def main():
    while True:
        try:
            X, Y = input("Fraction: ").strip().split("/")
            X = int(X)
            Y = int(Y)
            remain = round(X/Y * 100)

            if remain > 100:
                continue
            elif remain >= 99:
                print("F")
            elif remain <= 1:
                print("E")
            else:
                print(f"{remain}%")
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue

if __name__ == "__main__":
    main()
