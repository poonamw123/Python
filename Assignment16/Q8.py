# 8. Write a program which accept number from user and print that number of "*" on screen.
# Input : 5
# Output : * * * * *

def DisplayStar(num):
    for _ in range(num):
        print("*", end=" ")
    print()

if __name__ == "__main__":
    num = int(input("Enter number: "))
    DisplayStar(num)
