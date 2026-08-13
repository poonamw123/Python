import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def TrainModel(RandomValue, X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=RandomValue
    )
    
    Model = DecisionTreeClassifier(random_state=42)
    
    Model.fit(X_train, Y_train)
    
    Prediction = Model.predict(X_test)
    
    Accuracy = accuracy_score(Y_test, Prediction) * 100
    
    print("Random State : ", RandomValue)
    print("Testing Accuracy : ", Accuracy, "%")
    
    print("--------------------------------------")
    
def main():
    Data = pd.read_csv("student_performance_ml.csv")
        
    X = Data[["StudyHours",
                "Attendance",
                "PreviousScore",
                "AssignmentsCompleted",
                "SleepHours"]]
                
    Y = Data["FinalResult"]   
        
    TrainModel(0, X, Y)
    TrainModel(10, X, Y)
    TrainModel(42, X, Y)
         
if __name__ == "__main__":
    main()