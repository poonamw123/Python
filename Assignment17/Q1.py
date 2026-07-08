import Arithmetic

def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))

    print("Addition is :", Arithmetic.Add(no1, no2))
    print("Subtraction is :", Arithmetic.Sub(no1, no2))
    print("Multiplication is :", Arithmetic.Mult(no1, no2))
    print("Division is :", Arithmetic.Div(no1, no2))

if __name__ == "__main__":
    main()
