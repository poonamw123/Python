import pandas as pd
import matplotlib.pyplot as plt

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

    Model = DecisionTreeClassifier(
        max_depth=None,
        random_state=42
        )
    
    Model.fit(X_train, Y_train)
    
    # Training Prediction
    TrainPrediction = Model.predict(X_train)
    
    # Testing Prediction
    TestPrediction = Model.predict(X_test)
    
    # Calculate accuracy
    TrainAccuracy = accuracy_score(Y_train, TrainPrediction) * 100
    TestAccuracy = accuracy_score(Y_test, TestPrediction) * 100
    
    print("Training accuracy : ", TrainAccuracy, "%")
    print("Testing accuracy : ", TestAccuracy, "%")
    
    if TrainAccuracy == 100 and TestAccuracy < 100:
        print("\nObeservation : Model is overfitting")
    elif TrainAccuracy == TestAccuracy:
        print("\nObservation : Model is performing well")
    else:
        print("\nObservation : Model performance is accetable")
    
    
if __name__ == "__main__":
    main()