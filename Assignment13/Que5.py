def Grade(Marks):
    if Marks >= 75:
        print("Distinction")
        
    elif Marks >= 60:
        print("First Class")
        
    elif Marks >= 50:
        print("Second class")
        
    else:
        print("Fail")
        
def main():
    Marks = int(input("Enter marks : "))
    
    Grade(Marks)
    
if __name__ == "__main__":
    main()