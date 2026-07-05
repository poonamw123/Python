Display = lambda no : no % 3 == 0 and no % 5 == 0

def main():
    
    data = [3,15,30,20,45]
    print("input data is :", data)
    
    Fdata = list(filter(Display, data))
    print("numbers divisible by 3 and 5 are : ", Fdata)
    
    
if __name__ == "__main__":
    main()