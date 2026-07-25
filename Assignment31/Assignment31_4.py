import schedule
import time

def CreateLog():
    
    Border = "-" * 60
    
    timestamp = time.ctime()
    
    LogFileName = "Marvellous%s.log" % (timestamp)
    
    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_")
    
    print("Log file gets created with name : ", LogFileName)
    
    fobj = open(LogFileName, "w")
    
    fobj.write(Border + "\n")
    fobj.write("Marvellous Automation Script\n")
    fobj.write(Border + "\n\n")
    
    fobj.write("Log file created successfully\n")
    fobj.write("Creation Time : " + timestamp + "\n")
    
    fobj.write(Border + "\n")
    
    fobj.close()
    
def main():
    
    Border = "-" * 60
    
    print(Border)
    print("Marvellous Automation Script")
    print("Border")
    
    print("Automation Started...")
    
    schedule.every(10).minutes.do(CreateLog)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)    
    
if __name__ == "__main__":
    main()
    