def main():
    
    FileName = input("Enter file name : ")
    Word = input("Enter word to search : ")
    
    try:
        File = open(FileName, "r")
        
        Data = File.read()
        
        Count = Data.count(Word)
        
        print("Frequrncy of ", Word, "is", Count)
        
        File.close()
        
    except FileNotFoundError:
            print("File is not present in current directory")
            
        
        
if __name__ == "__main__":
    main()