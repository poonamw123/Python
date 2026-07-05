from functools import reduce

MaxNumber = lambda no1, no2 : no1 if no1>no2 else no2

def main():
    data = [2,45,89,50,53]
    print("input data is : ", data)
    
    Rdata = reduce(MaxNumber, data)
    print("Maxium number is : ", Rdata)
    
    
if __name__ == "__main__":
    main()