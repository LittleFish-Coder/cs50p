def main():
    MONTH = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    while True:
        try:
            date = input("Date: ").strip().title()
            if "/" in date:
                month, day, year = date.split("/")
            elif "," in date:
                date = date.replace(",", "")
                month, day, year = date.split(" ")
                month = MONTH[month]

            if not 0 <= int(month) <= 12:
                continue
            if not 1 <= int(day) <= 31:
                continue

            print(f"{int(year)}-{int(month):02}-{int(day):02}")
            break
        except:
            pass


if __name__ == "__main__":
    main()

