def Area(Radius):
    PI = 3.14
    Ans = PI * Radius * Radius
    return Ans

def main():
    Radius = float(input("Enter radius : "))
    Ret = Area(Radius)
    print("Area of circle is : ", Ret)
    
    
if __name__ == "__main__":
    main()
    