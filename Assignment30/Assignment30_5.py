import schedule
import time
import datetime

def Display():
    fobj = open("Marvellous.txt", "a")
    
    fobj.write("Task executed at : ")
    
    fobj.write(str(datetime.datetime.now()))
    
    fobj.write("\n")
    
    fobj.close()
    
    print("Data written successfully")
    
def main():
    print("Automation started")
    
    schedule.every(5).minutes.do(Display)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()
    