def sum_of_digits(n):
    sum_digits = 0
    n = abs(n)
    while n > 0:
        sum_digits += n % 10
        n //= 10
    return sum_digits

def main():
    n = int(input("Enter number: "))
    print("Sum of digits:", sum_of_digits(n))

if __name__ == "__main__":
    main()
