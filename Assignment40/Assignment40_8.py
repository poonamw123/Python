import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree


def main():
    

    Data = pd.read_csv("student_performance_ml.csv")
    
    
    X = Data[["StudyHours",
                  "Attendance",
                  "PreviousScore",
                  "AssignmentsCompleted",
                  "SleepHours"]]
        
    Y = Data["FinalResult"]
    
       
    X_train, X_test, Y_train, Y_test = train_test_split(
            X,
            Y,
            test_size=0.2,
            random_state=42
        )

    Model = DecisionTreeClassifier(random_state=42)
    Model.fit(X_train, Y_train)
    
    plt.figure(figsize=(15,8))
    
    plot_tree(
        Model,
        feature_names=X.columns,
        class_names=["Fail", "Pass"],
        filled=True,
        rounded=True,
        fontsize=10
    )
    
    plt.title("Decision Tree Visualization")
    plt.show()
    
if __name__ == "__main__":
    main()