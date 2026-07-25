import os
import sys
import shutil
import schedule
import time

def CopyFiles(SourceDir, DestinationDir):
    
    if not os.path.exists(SourceDir):
        print("Source directory does not exist")
        return
    
    if not os.path.exists(DestinationDir):
        print("Destination directory does not exist")
        return
    
    LogFile = open("CopyLog.txt", "a")
    
    LogFile.write("\n--------------------------------------\n")
    LogFile.write("Copy Time : "+ time.ctime() + "\n")
    
    for FolderName, SubFolder, FileNames in os.walk(SourceDir):
        
        for File in FileNames:
            
            if File.endswith(".txt"):
                SourceFile = os.path.join(FolderName, File)
                DestinationFile = os.path.join(DestinationDir, File)
                
                try:
                    shutil.copy(SourceFile, DestinationFile)
                    
                    print(File, "Copied")
                    
                    LogFile.write(File + "Copied Successfully\n")
                    
                except Exception as e:
                    print(File, "Not Copied")
                    
                    LogFile.write(File + " : "+str(e) + "\n")
                    
        LogFile.close()
        
def main():
    Border = "-" * 60
    
    print(Border)
    print("Marvellous Automation Script")
    print(Border)
    
    if len(sys.argv) != 3:
        print("Usage : python Program.py SourceDirectory DestinationDirectory")
        return
    
    schedule.every(10).minutes.do(CopyFiles, sys.argv[1], sys.argv[2])
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()