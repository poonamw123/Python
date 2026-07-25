import time
import schedule

FileName = input("Enter filename : ")

def ReadFile():
    
    try:
        fobj = open(FileName, "r")
        
        Data = fobj.read()
        
        if len(Data)==0:
            print("File is empty")
        else:
            print(Data)
            
        fobj.close()
        
    except FileNotFoundError:
        print("File does not exist")
        
    except PermissionError:
        print("Permission denied")
        
    except:
        print("Unable to open file")
        
def main():
    
    schedule.every(1).minutes.do(ReadFile)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()