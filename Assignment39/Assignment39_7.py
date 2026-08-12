import pandas as pd
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
    
    Model = DecisionTreeClassifier()
    
    Model.fit(X_train, Y_train)
    
    Student = [[6, 85, 66, 7, 7]]
    
    Prediction = Model.predict(Student)
    
    if Prediction[0] == 1:
        print("Student will pass")
        
    else:
        print("Student will fail")
    
    
    
if __name__ == "__main__":
    main()