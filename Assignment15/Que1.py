Square = lambda No : No*No

def main():
    
    Data = [1,2,3,4,5]
    print("Input data is : ", Data)
    
    MData = list(map(Square, Data))
    
    print("Square of each number is : ", MData)
    
    
    
if __name__ == "__main__":
    main()