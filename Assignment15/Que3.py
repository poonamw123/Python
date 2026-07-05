Odd = lambda No : No % 2 != 0

def main():
    
    Data = [1,2,3,4,5,6,7,8,9]
    
    print("Input data is : ", Data)
    
    FData = list(filter(Odd, Data))
    
    print("List of odd numners after filter is : ", FData)
    
    
if __name__ == "__main__":
    main()