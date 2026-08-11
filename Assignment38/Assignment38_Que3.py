import pandas as pd

def main():
    Data = pd.read_csv("student_performance_ml.csv")
    
    print("Average studyhours : ", Data["StudyHours"].mean())
    
    print("Average Attendance : ", Data["Attendance"].mean())
    
    print("Maximum PreviousScore : ", Data["PreviousScore"].max())
    
    print("Minimum SleepHours : ", Data["SleepHours"].min())
    
    
if __name__ == "__main__":
    main()