import sys

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python program.py ABC.txt")
        return
    
    SourceFile = sys.argv[1]
    
    try:
        Source = open(SourceFile, "r")
        
        Destination = open("Demo.txt", "w")
        
        Data = Source.read()
        Destination.write(Data)
        
        print("Contents copied successfully.")
        
        Source.close()
        Destination.close()
        
    except FileNotFoundError:
        print("File is not present in current directory")
        
    
    
if __name__ == "__main__":
    main()