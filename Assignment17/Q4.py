def sum_of_factors(n):
    sum_factors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_factors += i
    return sum_factors

def main():
    n = int(input("Enter number: "))
    print("Sum of factors is:", sum_of_factors(n))

if __name__ == "__main__":
    main()
