import time
import schedule
import datetime

def CreateFile():
    timestamp = datetime.datetime.now()
    
    FileName = "File%s.txt"%(timestamp)
    FileName = FileName.replace(" ", "_")
    FileName = FileName.replace(":", "_")
    FileName = FileName.replace(".", "_")
    
    fobj = open(FileName, "w")
    
    fobj.write("File Name : " +FileName+"\n")
    fobj.write("Creation Date : "+timestamp.strftime("%d-%m-%Y")+"\n")
    fobj.write("Creation Time : "+timestamp.strftime("%I:%M:%S %p")+"\n")
    
    fobj.close()
    
    print("File created : ", FileName)
    
def main():
    print("Automation script started")
    
    schedule.every(1).minute.do(CreateFile)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()
    