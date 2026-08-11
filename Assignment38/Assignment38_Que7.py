import pandas as pd
import matplotlib.pyplot as plt

def main():
    Data = pd.read_csv("student_performance_ml.csv")
    
    Passed = Data[Data["FinalResult"] == 1]
    Failed = Data[Data["FinalResult"] == 0]
    
    plt.scatter(Passed["StudyHours"], Passed["PreviousScore"], label = "Pass")
    
    plt.scatter(Failed["StudyHours"], Failed["PreviousScore"], label = "Fail")
    
    
    plt.title("Study Hours vs Previous Score")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.grid(True)
    
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()