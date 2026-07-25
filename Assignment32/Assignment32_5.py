import sys
import os
import time
import schedule

def DeleteEmptyFiles(DirectoryPath):
    
    Border = "-" * 60
    
    timestamp = time.ctime()
    
    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")
    
    Ret = False
    
    Ret = os.path.exists(DirectoryPath)
    
    if(Ret == False):
        print("Marvellous Automation Error : There is no such directory with name", DirectoryPath)
        return
    
    Ret = os.path.isdir(DirectoryPath)
    
    if(Ret == False):
        print("Marvellous Automation Error : It is not a directory with name", DirectoryPath)
        return
    
    
    print("Log File gets created with name : ", LogFileName)
    
    fobj = open(LogFileName, "w")
    
    fobj.write(Border+"\n")
    
    fobj.write("Marvellous Automation Script \n")
    fobj.write(Border+"\n\n")
    
    fobj.write("Deleted Empty Files\n")
    fobj.write(Border+"\n\n")
    
    Count = 0
    
    for FolderName, SubFolder, FileNames in os.walk(DirectoryPath):
        
        for fname in FileNames :
            fname = os.path.join(FolderName, fname)
            
            try:
                if(os.path.getsize(fname) == 0):
                    os.remove(fname)
                    
                    Count = Count + 1
                    
                    print("Deleted: ", fname)
                    
                    fobj.write(fname+"\n")
                    
            except PermissionError:
                print("Permission denied : ", fname)
                
                fobj.write("Permission denied : "+fname+"\n")
                
    fobj.write("\n")
    fobj.write("Total deleted files : "+str(Count)+"\n")
    fobj.write("Log file gets created at : "+timestamp+"\n")
    fobj.write(Border)
    
    fobj.close()
    
def main():
    Border = "-"*60
    print(Border)
    print("Marvellous Automation Script")
    print(Border)
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("This automation script is used to travel directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U" ):
            print("Please execute the script as ")
            print("python FileName.py DirectoryName")
            print("Directory name should be absolute path")
        else:
            schedule.every(10).seconds.do(DeleteEmptyFiles, sys.argv[1])
            
            while True:
                schedule.run_pending()
                time.sleep(1)
    else:       
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")
    
    print(Border)
    print("Thank you for using Marvellous Automation Script")
    print(Border) 
    
    
if __name__ == "__main__":
    main()
            