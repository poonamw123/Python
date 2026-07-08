# 10. Write a program which accept name from user and display length of its name.
# Input : Marvellous
# Output : 10

def DisplayLength(name):
    return len(name)

if __name__ == "__main__":
    name = input("Enter name: ")
    print(DisplayLength(name))
