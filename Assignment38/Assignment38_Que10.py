import pandas as pd
import matplotlib.pyplot as plt

def main():
    Data = pd.read_csv("student_performance_ml.csv")
    
    plt.scatter(
        Data["SleepHours"],
        Data["FinalResult"],
        color="purple",
        s=100,
        marker="o",
        alpha=0.8,
        edgecolors="black",
        linewidths=1,
        label = "Students"
    )
    
    plt.title("Sleep Hours vs Final Result")
    plt.xlabel("Sleep Hours")
    plt.ylabel("Final Result")
    plt.grid(True)
    plt.legend()
    
    plt.show()
    
if __name__ == "__main__":
    main()