def ReverseDisplay(No):
    for i in range(No, 0, -1):
        print(i, end = " ")
        
def main():
    Value = int(input("Enter a number : "))
    
    ReverseDisplay(Value)
    
if __name__ == "__main__":
    main()