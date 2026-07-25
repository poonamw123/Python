import os
import schedule
import time
import datetime

def DirectoryCount(DirectoryPath):
    
    Count = 0
    
    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        Count = Count + len(FileName)
    
    fobj = open("DirectoryCountLog.txt", "a")
    
    fobj.write("--------------------------------------------\n")
    fobj.write("Directory Path : " + DirectoryPath + "\n")
    fobj.write("Number of Files : " + str(Count) + "\n")
    fobj.write("Date and Time : " + str(datetime.datetime.now()) + "\n")
    fobj.write("--------------------------------------------\n\n")
    
    fobj.close()
    
    print("Entry added successfully")
    
def main():
    
    DirectoryPath = input("Enter directory path : ")
    
    schedule.every(5).minutes.do(DirectoryCount, DirectoryPath)
    
    print("Directory monitoring started...")
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
    
if __name__ == "__main__":
    main()