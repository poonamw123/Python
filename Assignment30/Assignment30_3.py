import schedule
import time

def Display():
    print("Coding kar..!")
    
def main():
    print("Automation script started")
    
    schedule.every(30).minutes.do(Display)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
    print("End of automation script")
    
if __name__ == "__main__":
    main()