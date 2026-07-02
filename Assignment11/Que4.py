def Reverse(No):
    Rev = 0
    
    while No > 0:
        Digit = No % 10
        Rev = (Rev * 10) + Digit
        No = No // 10
        
    return Rev

def main():
    Value = int(input("Enter a number : "))
    
    Ret = Reverse(Value)
    
    print("Reverse of number : ", Ret)
    
if __name__ == "__main__":
    main()