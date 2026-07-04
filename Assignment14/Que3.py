MaxNumber = lambda No1, No2 : No1 if No1>No2 else No2

def main():
    
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    
    Ret = MaxNumber(Value1, Value2)
    
    print("Maximum number is : ", Ret)
    
    
if __name__ == "__main__":
    main()