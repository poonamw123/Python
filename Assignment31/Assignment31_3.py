import sys
import schedule
import time
import datetime
import os

def DirectoryScanner(DirectoryPath):
    
    Files = 0
    Directories = 0
    
    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        Files = Files + len(FileName)
        Directories = Directories + len(SubFolder)
        
    print("----------------------------------------------------------")
    
    print("Directory Scanned : ", DirectoryPath)
    print("Total Files : ", Files)
    print("Total Subdirectories : ", Directories)
    print("Scan time : ", datetime.datetime.now())
    
    print("----------------------------------------------------------")
    
def main():
    
    Border = "-" * 60
    
    print(Border)
    print("Automation script")
    print(Border)
    
    if(len(sys.argv) == 2):
        
        if(sys.argv[1] == "-h" or sys.argv[1] == "-H"):
            print("This automation script scans a directory every minute.")
            print("Use -u flag for usage.")
            
        elif(sys.argv[1] == "-u" or sys.argv[1] == "-U"):
            print("Usage : ")
            print("python Assignment31_3.py DirectoryPath")
            print("Example : ")
            print("python Assignment31_3.py D:\\Data")
            
        else:
            if(os.path.exists(sys.argv[1]) == False):
                print("Directory does not exists")
                return
            print("Automation Started...")
            
            schedule.every(10).seconds.do(DirectoryScanner, sys.argv[1])
            
            while True:
                schedule.run_pending()
                time.sleep(1)
                
            else:
                print("Invalid number of arguments")
                print("Please use -h or -u option")
                
            print(Border)
            print("Thank you for using Automation script")
            print(Border)
            
              
if __name__ == "__main__":
    main()
            