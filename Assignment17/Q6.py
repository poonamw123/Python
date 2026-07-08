def display_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def main():
    n = int(input("Enter number: "))
    display_pattern(n)

if __name__ == "__main__":
    main()
