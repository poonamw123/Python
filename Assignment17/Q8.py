def display_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main():
    n = int(input("Enter number: "))
    display_pattern(n)

if __name__ == "__main__":
    main()
