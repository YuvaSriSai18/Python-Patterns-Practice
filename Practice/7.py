def main():
    total = 0
    while True:
        try:
            num = float(input("Enter a number (or 0 to stop): "))
            if num == 0:
                break
            total += num
        except ValueError:
            print("Please enter a valid number.")

    print(f"The sum of the numbers entered is: {total}")

if __name__ == "__main__":
    main()
