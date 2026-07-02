def Factorial(No):
    
    Multiplication = 1
    
    for i in range(1, No+1):
        Multiplication = Multiplication * i
        
    return Multiplication    
    
def main():
    
    Value = int(input("Enter a number : "))
    
    Ret = Factorial(Value)
    
    print("Factorial is : ", Ret)
    
    
if __name__ == "__main__":
    main()