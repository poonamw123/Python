import os
import time
import schedule
import datetime

FilePath = input("Enter file path : ")

def CheckFile():
    
    fobj = open("FileSizeLog.txt", "a")
    
    if os.path.exists(FilePath):
        
        Size = os.path.getsize(FilePath)
        
        fobj.write("File : "+FilePath+"\n")
        fobj.write("Size : "+str(Size)+"Bytes\n")
        fobj.write("Time : "+str(datetime.datetime.now())+"\n")
        fobj.write("--------------------------------\n")
        
        print("Logged successfully")
        
    else:
        print("File does not exist")
        
    fobj.close()
    
def main():
    schedule.every(30).seconds.do(CheckFile)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()