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
    
    Prediction = Model.predict(X_test)
    
    Misclassified = X_test[Y_test != Prediction]
    
    print("Misclassified Students")
    print("----------------------------------------")
    
    if len(Misclassified) == 0:
        print("No misclassified students found.")
    else:
        print(Misclassified)
        
    print("\nNumber of misclassified students : ", len(Misclassified))
    
    #Observation:
    if len(Misclassified) == 0: 
        print("\nObeservation : ")
        print("Model classified all students correctly")
        print("Testing accuracy = 100%")
    
    else:      
        print("\nObeservation : ")
        print("Some students were classified incorrectly.")
        print("These students have feature values that are difficult for the model to separate")
    
if __name__ == "__main__":
    main()