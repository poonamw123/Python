add = lambda No1,No2 : No1+No2

def main():
    Value1 = int(input("enter first number : "))
    Value2 = int(input("enter second number : "))
    
    Ret = add(Value1, Value2)
    
    print("Addition is : ", Ret)
    
if __name__ == "__main__":
    main()