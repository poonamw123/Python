def count_digits(n):
    if n == 0:
        return 1
    count = 0
    n = abs(n)
    while n > 0:
        count += 1
        n //= 10
    return count

def main():
    n = int(input("Enter number: "))
    print("Number of digits:", count_digits(n))

if __name__ == "__main__":
    main()
