def main():
    try:
        ExistingFile = open("ABC.txt", "r")
        NewFile = open("Demo.txt", "w")
        
        print("Both files opened successfully")
        
        Data = ExistingFile.read()
        NewFile.write(Data)
        
        print("Contents copied successfully")
        
        ExistingFile.close()
        NewFile.close()
        
    except FileNotFoundError:
        print("Existing file is not present")
        
if __name__ == "__main__":
    main()