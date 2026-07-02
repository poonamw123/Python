def DivisibleBy3(No):
    if(No % 3 & No % 5 == 0):
        return True
    
    else:
        return False
        

def main():
    Value = int(input("Enter a number : "))
    
    Ret = DivisibleBy3(Value)
    
    if Ret == True:
        print("It is divisble by 3 and 5")
        
    else:
        print("It is not divisble by 3 and 5")
        

if __name__ == "__main__":
    main()