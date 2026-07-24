import schedule
import time
import shutil
import datetime
import os

def Backup():
    
    Source = input("Enter source file path: ")
    Destination = input("Enter destination folder: ")
    
    FileName = os.path.basename(Source)
    
    TimeStamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    
    NewFile = Destination + "\\" + TimeStamp + "_" + FileName
    
    shutil.copy(Source, NewFile)
    
    Log = open("backup_log.txt", "a")
    
    Log.write("Backup completed successfully at ")
    
    Log.write(str(datetime.datetime.now()))
    
    Log.write("\n")
    
    Log.close()
    
    print("Backup completed successfully")
    
def main():
    
    print("Automation started")
    
    schedule.every().hour.do(Backup)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()