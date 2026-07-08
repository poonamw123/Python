# 7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
# Input : 8
# Output : False
# Input : 25
# Output : True

def CheckDivisibleBy5(num):
    if num % 5 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    num = int(input("Enter number: "))
    ans = CheckDivisibleBy5(num)
    print(ans)
