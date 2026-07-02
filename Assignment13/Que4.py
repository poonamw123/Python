def Binary(No):
    print("Binary Equivalent = ", bin(No)[2 : ])
    
def main():
    Value = int(input("Enter a number : "))
    
    Binary(Value)
    
if __name__ == "__main__":
    main()