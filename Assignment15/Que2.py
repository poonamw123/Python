Even = lambda No : No%2==0

def main():
    
    Data = [2,4,5,7,8,9]
    print("Input data is : ", Data)
    
    FData = list(filter(Even, Data))
    print("list of even numbers after filter is : ", FData)    
    
if __name__ == "__main__":
    main()