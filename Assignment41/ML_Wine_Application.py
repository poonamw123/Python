import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    # Step 1 : Get Data
    Data = pd.read_csv("WinePredictor.csv")
    

    # Step 2 : Clean, Prepare and Manipulate data
    X = Data.drop("Class", axis=1)
    Y = Data["Class"]

    # Step 3 : Train Data
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    # Step 4 : Train Model
    Model = DecisionTreeClassifier(random_state=42)
    Model.fit(X_train, Y_train)

    # Step 5 : Test Data
    Prediction = Model.predict(X_test)

    # Step 6 : Calculate Accuracy
    Accuracy = accuracy_score(Y_test, Prediction) * 100
    print("Accuracy : ", Accuracy, "%")
    
if __name__ == "__main__":
    main()


