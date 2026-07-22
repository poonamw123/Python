def main():
    try:
        fobj = open("Demo.txt", "r")
        print("File gets opened")
        
        Count = 0
        
        for line in fobj:
            Words = line.split()
            Count = Count + len(Words)
            
        print("Total number of words : ", Count)
        
        fobj.close()
            
    except FileNotFoundError:
        print("File is not present in current directory")
        


if __name__ == "__main__":
    main()