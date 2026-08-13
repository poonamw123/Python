import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


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
    
    NewStudents = pd.DataFrame({
        "StudyHours":[6,3,8,5,2],
        "Attendance":[85,60,95,75,55],
        "PreviousScore":[66,45,80,62,40],
        "AssignmentsCompleted":[7,3,6,10,2],
        "SleepHours":[7,6,8,7,5]
        
    })
    
    Prediction = Model.predict(NewStudents)
    
    NewStudents["Prediction"] = Prediction
    
    print(NewStudents)
    
if __name__ == "__main__":
    main()