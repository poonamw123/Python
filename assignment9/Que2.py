def ChkGreater(No1,No2):
    if(No1 > No2):
        return True
    else:
        return False
    
def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number : "))
    
    Ret = ChkGreater(Value1, Value2)
    
    if Ret : 
        print(Value1, " is greater number")
    else:
        print(Value2, "is greater number")
        
    
if __name__ == "__main__":
    main()