from functools import reduce

Addition = lambda No1, No2 : No1 + No2

def main():
    Data = [2,4,3,6,7]
    
    print("Input data is : ", Data)
    
    RData = reduce(Addition, Data)
    
    print("Addition of all elements is : ", RData)
     
    
if __name__ == "__main__":
    main() 