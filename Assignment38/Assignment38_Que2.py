import pandas as pd

def main():
    Data = pd.read_csv("student_performance_ml.csv")
    
    TotalStudents = len(Data)
    
    PassedStudents = len(Data[Data["FinalResult"] == 1])
    
    FailedStudents = len(Data[Data["FinalResult"] == 0])
    
    print("--------------- Student Performance Report ----------------")
    
    print("Total students : ", TotalStudents)
    print("Passed students : ", PassedStudents)
    print("Failed students : ", FailedStudents)
    
    
if __name__ == "__main__":
    main()