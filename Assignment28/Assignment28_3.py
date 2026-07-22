def main():
    try:
        fobj = open("Demo.txt", "r")
        print("File gets opened")
        
        for line in fobj:
            print(line, end="")
            
        fobj.close()
        
    except FileNotFoundError:
        print("File is not present in current directory")
        
if __name__ == "__main__":
    main()
    
    