import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def main():
    
    # Load Dataset
    Data = pd.read_csv("student_performance_ml.csv")
    
    # Input and Output
    X = Data[["StudyHours",
                  "Attendance",
                  "PreviousScore",
                  "AssignmentsCompleted",
                  "SleepHours"]]
        
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
    
    # Feature Importance
    print("\nFeature Importance Scores")
    
    Importance = Model.feature_importances_
    
    Features = X.columns
    
    for Name, Score in zip(Features, Importance):
        print(Name, ":", round(Score, 4))
        
    # Most important feature
    MaxIndex = Importance.argmax()
    print("\nMost Important Feature : ", Features[MaxIndex])
    
    #Least important feature
    MinIndex = Importance.argmin()
    print("Least Important feature : ", Features[MinIndex])
    
if __name__ == "__main__":
    main()