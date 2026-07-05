Strings = lambda s : len(s) > 5

def main():
    
    data = ["Physics", "Chemistry", "Maths", "History"]
    
    print("Input data is : ", data)
    
    Fdata = list(filter(Strings, data))
    
    print("Lists of strings having lenght greater than 5 is : ", Fdata)
    
    
if __name__ == "__main__":
    main()