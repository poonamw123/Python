import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score

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
    
    Depth = [1, 3, None]
    
    for Value in Depth:
        Model = DecisionTreeClassifier(max_depth=Value)
        
        Model.fit(X_train, Y_train)
        
        Prediction = Model.predict(X_test)
        
        Accuracy = accuracy_score(Y_test, Prediction)
        
        print("Max Depth : ", Value)
        print("Testing Accuracy : ", Accuracy * 100, "%")
        
    print("----------------------------------")
    
    
    
if __name__ == "__main__":
    main()