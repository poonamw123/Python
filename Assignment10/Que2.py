def Sum(No):
    
    Addition = 0
    
    for i in range(1, No+1):
        Addition = Addition + i
        
    return Addition
    
    
def main():
    Value = int(input("Enter a number : "))
    
    Ret = Sum(Value)
    
    print("Sum of first natural numbers is : ", Ret)
    
    
if __name__ == "__main__":
    main()