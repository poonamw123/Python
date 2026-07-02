def Display(No1, No2):
    print("Addition is : ", No1+No2)
    print("Substraction is : ", No1-No2)
    print("Multiplication is : ", No1*No2)
    print("Division is : ", No1/No2)
    
def main():
    Value1 = int(input("Enter first number : " ))
    Value2 = int(input("Enter second number : "))
    
    Display(Value1, Value2)
    
if __name__ == "__main__" :
    main()