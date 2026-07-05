even = lambda no : no % 2 == 0

def main():
    data = [2,4,5,6,7,8]
    print("input data is : ", data)
    
    Fdata = list(filter(even, data))
    print("Count of even numbers is : ", len(Fdata))
    
    
if __name__ == "__main__":
    main()