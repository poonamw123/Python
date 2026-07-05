from functools import reduce

MinNumber = lambda no1, no2 : no1 if no1<no2 else no2

def main():
    data = [2,45,65,34,21]
    print("input data is : ", data)
    
    Rdata = reduce(MinNumber, data)
    
    print("Minimum number is : ", Rdata)
    
    
if __name__ == "__main__":
    main()