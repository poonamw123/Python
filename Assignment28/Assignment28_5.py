import sys

def main():
    try:
        fobj = open(sys.argv[1], "r")
        print("File gets opened")
        
        Data = fobj.read()
        
        if sys.argv[2] in Data:
            print(sys.argv[2], "is present in", sys.argv[1])
            
        else:
            print(sys.argv[2], "is not present in", sys.argv[1])
            
        fobj.close()
        
    except FileNotFoundError:
        print("File is not present in current directory")
        
if __name__ == "__main__":
    main()