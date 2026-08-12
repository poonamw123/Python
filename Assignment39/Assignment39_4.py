import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

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
    
    Prediction = Model.predict(X_test)
    
    Matrix = confusion_matrix(Y_test, Prediction)
    
    Display = ConfusionMatrixDisplay(confusion_matrix=Matrix)
    
    Display.plot()
    
    plt.title("Confusion Matrix")
    
    plt.show()
    
if __name__ == "__main__":
    main()