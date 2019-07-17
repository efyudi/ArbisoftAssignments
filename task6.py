def show_stars(rows):
    for i in range(0, rows + 1):
        for j in range(0, i):
            print("*", end="")
        print("")


if __name__ == "__main__":
    rows = int(input("Enter Number of Rows : "))
    show_stars(rows)
