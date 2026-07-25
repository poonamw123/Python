import schedule
import time

def MondayTask():
    print("Start your weekly goals")
    
def WednesdayTask():
    print("Review your weekly progress")
    
def FridayTask():
    print("Weekly work completed")
    
def main():
    
    print("Automation script started")
    
    # Monday at 9.00 AM
    
    schedule.every().monday.at("09:00").do(MondayTask)
    
    #Wednesday at 5:00 PM
    
    schedule.every().wednesday.at("17:00").do(WednesdayTask)
    
    #Friday at 6:00 PM
    schedule.every().friday.at("18:00").do(FridayTask)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()