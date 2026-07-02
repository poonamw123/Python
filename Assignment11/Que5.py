def Palindrome(No):
    Temp = No
    Rev = 0

    while Temp > 0 : 
        Digit = Temp % 10
        Rev = (Rev * 10) + Digit
        Temp = Temp // 10
        
    if No == Rev : 
        return True
    
    else: 
        return False
    
def main():
    Value = int(input("Enter a number : "))
    
    Ret = Palindrome(Value)
    
    if Ret:
        print("it is Palindrome")
        
    else:
        print("it is not a Palindrome")
        
if __name__ == "__main__":
    main()
