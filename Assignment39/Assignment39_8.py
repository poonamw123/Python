import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

def main():
    
    # Step 1 : Load Dataset
    Data = pd.read_csv("student_performance_ml.csv")
    
    print("First 5 Records")
    print(Data.head())

    # Step 2 : Data Analysis
    print("\nTotal Students : ", len(Data))
    print("Passed students : ", len(Data[Data["FinalResult"] == 1]))
    print("Failed students : ", len(Data[Data["FinalResult"] == 0]))
    
    # Step 3 : Visualization
    plt.hist(Data["StudyHours"], bins = 5, edgecolor = "black")
    plt.title("Study Hours Distribution")
    plt.xlabel("Study Hours")
    plt.ylabel("Number of Students")
    plt.show()
    
    # Step 4 : Train-Test Split
    
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
    
    # Step 5 : Model Training
    Model = DecisionTreeClassifier()
    Model.fit(X_train, Y_train)
    
    print("\nModel trained successfully")
    
    # Step 6 : Prediction
    Prediction = Model.predict(X_test)
    print("\nPredicted Values")
    print(Prediction)
    
    # Step 7 : Accuracy
    Accuracy = accuracy_score(Y_test, Prediction)
    print("\nModel Accuracy : ", Accuracy * 100, "%")
    
    # Step 8 : Confusion Matrix
    Matrix = confusion_matrix(Y_test, Prediction)
    
    Display = ConfusionMatrixDisplay(confusion_matrix=Matrix)
    Display.plot()
    plt.title("Confusion Matrix")
    plt.show()
    
    # Step 9 : Final Conclusion
    print("\nConclusion")
    print("Decision tree model successfully predicted student performance")
    print("The model achieved good accuracy on the given dataset")
    
if __name__ == "__main__":
    main()