def ChkPerfect(No) : 
    Sum = 0
    
    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i
            
    if Sum == No:
        return True
    
    else : 
        return False
    
def main():
    Value = int(input("Enter a number : "))
    
    Ret = ChkPerfect(Value)
    
    if Ret :
        print("Perfect number")
        
    else:
        print("Not a perfect number")
        
if __name__ == "__main__":
    main()