# 3. Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
# Input : 11  5
# Output : 16

def Add(no1, no2):
    return no1 + no2

if __name__ == "__main__":
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
    ans = Add(no1, no2)
    print("Addition is :", ans)
