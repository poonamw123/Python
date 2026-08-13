import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def main():
    
    # Load Dataset
    Data = pd.read_csv("student_performance_ml.csv")
    
    # SleepHours colunm removed
    X = Data[["StudyHours",
                  "Attendance",
                  "PreviousScore",
                  "AssignmentsCompleted"]]
        
    Y = Data["FinalResult"]
    
     # Train-Test Split   
    X_train, X_test, Y_train, Y_test = train_test_split(
            X,
            Y,
            test_size=0.2,
            random_state=42
        )
    
    # Model Training
    Model = DecisionTreeClassifier(random_state=42)
    Model.fit(X_train, Y_train)
    
    print("Decision Tree Model Trained Successfully")
    
    Prediction = Model.predict(X_test)
    
    Accuracy = accuracy_score(Y_test, Prediction)
    
    print("Accuracy after removing Sleephours : ", Accuracy * 100, "%")
    
if __name__ == "__main__":
    main()