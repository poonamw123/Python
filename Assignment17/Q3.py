def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def main():
    n = int(input("Enter number: "))
    print("Factorial is:", factorial(n))

if __name__ == "__main__":
    main()
