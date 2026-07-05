from functools import reduce

product = lambda no1,no2 : no1*no2

def main():
    
    data = [2,3,4,5,6]
    print("input data is : ", data)
    
    Rdata = reduce(product, data)
    print("Product of all numbers is : ", Rdata)
    
    
if __name__ == "__main__":
    main()