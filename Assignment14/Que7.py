Divisibleby5 = lambda No : (No % 5 == 0)

def main():
    Value = int(input("enter a number : "))
    
    print(Divisibleby5(Value))
    
if __name__ == "__main__":
    main()
