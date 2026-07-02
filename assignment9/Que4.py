def Cube(No):
    return No*No*No


def main():
    Value = int(input("Enter a number : "))
    
    Ret = Cube(Value)
    
    print("Cube is : ", Ret)


if __name__ == "__main__":
    main()