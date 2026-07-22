import sys

def main():
    
    if len(sys.argv) != 3:
        print("Usage: python program.py File1.txt File2.txt")
        return
    
    try:
        File1 = open(sys.argv[1], "r")
        File2 = open(sys.argv[2], "r")
        
        Data1 = File1.read()
        Data2 = File2.read()
        
        if Data1 == Data2:
            print("success")
            
        else:
            print("Failure")
            
        File1.close()
        File2.close()
        
    except FileNotFoundError : 
        print("File is not present in current directory")
        
if __name__ == "__main__":
    main()