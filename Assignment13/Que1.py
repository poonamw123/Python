def Area(Length, Width):
    Ans = Length * Width
    return Ans

def main():
    Length = int(input("Enter length : "))
    Width = int(input("Enter width : "))
    
    Ret = Area(Length, Width)
    
    print("Area of rectangle is : ", Ret)
    
    
if __name__ == "__main__":
    main()