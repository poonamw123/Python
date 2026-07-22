def main():
    Filename = input("Enter filename : ")
    
    try:
        fobj = open(Filename, "r")
        print("File gets opened")
        
        Data = fobj.read()
        
        print("File contents :")
        print(Data)
        
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File is not present in current directory")
    
    
if __name__ == "__main__":
    main()