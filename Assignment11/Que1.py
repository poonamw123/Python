def Prime(No):
    if No <= 1 : 
        return False
    
    for i in range(2, No):
        if No % i == 0:
            return False
        
    return True

def main():
    Value = int(input("Enter a number : "))
    
    Ret = Prime(Value)
    
    if Ret : 
        print("It is a prime number")
        
    else : 
        print("It is not a prime number")
        
if __name__ == "__main__":
    main()