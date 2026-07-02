def MultTable(No):
    for i in range(1, 11):
        print(No * i, end = " ")

def main():
    Value = int(input("enter a number : "))
    
    MultTable(Value)

if __name__ == "__main__":
    main()