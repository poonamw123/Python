import pandas as pd
import matplotlib.pyplot as plt

def main():
    Data = pd.read_csv("student_performance_ml.csv")
    
    plt.hist(Data["StudyHours"],
            bins = 5,
            edgecolor = "black",
            alpha = 0.8,
            rwidth=0.9
            )
    
    plt.title("Study Hours Distribution")
    plt.xlabel("Study Hours")
    plt.ylabel("Number of Students")
    
    plt.show()
    
    
if __name__ == "__main__":
    main()
    

# Observation  :The histogram shows that most students study between 4 and 8 hours per day.
# Very few students study extremely low hours. 
# The distribution indicates that study hours are spread across the dataset, with more students in the higher study-hour range
