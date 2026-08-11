import pandas as pd

def main():
    Data = pd.read_csv("student_performance_ml.csv")
    
    print(Data.groupby("FinalResult")[["StudyHours", "Attendance"]].mean())
    
if __name__ == "__main__":
    main()
    
    
#Observation : 
# Students who study more hours generally have a higher chance of passing
# Students with higher attendance also tend to perform better
# Both StudyHours and Attendance positively influence the FinalResult
# However, these are not the only factors affecting the FinalResult
