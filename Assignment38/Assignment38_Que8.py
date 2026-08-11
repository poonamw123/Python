import pandas as pd
import matplotlib.pyplot as plt

def main():
    Data = pd.read_csv("student_performance_ml.csv")
    
    plt.boxplot(
        Data["Attendance"],
        patch_artist=True
    )
    
    plt.title("Attendance Boxplot")
    plt.ylabel("Attendance")
    
    plt.grid(True)
    
    plt.show()
    
if __name__ == "__main__":
    main()