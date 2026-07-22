import os

def main():
    Filename = input("Enter filename: ")
    
    if(os.path.exists(Filename)):
        print("file is present in current directory")
        
    else:
        print("There is no such file")
    
    
    
if __name__ == "__main__":
    main()