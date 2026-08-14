import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def CheckAccuracy(X, Y):

    print("----------------------------------------")
    print("Accuracy using different values of K")
    print("----------------------------------------")

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size = 0.5,
        random_state = 42
    )

    for K in [1,3,5]:

        Model = KNeighborsClassifier(n_neighbors = K)

        Model.fit(X_train, Y_train)

        Prediction = Model.predict(X_test)

        Accuracy = accuracy_score(Y_test, Prediction) * 100

        print("K =",K," Accuracy =",Accuracy,"%")

def main():

    Border = "-" * 50

    print(Border)
    print("Marvellous Infosystems Play Predictor")
    print(Border)

    # Step 1 : Load Dataset
    Data = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

    print("Dataset")
    print(Border)
    print(Data)
    print(Border)

    # Step 2 : Label Encoding
    WeatherEncoder = LabelEncoder()
    TemperatureEncoder = LabelEncoder()
    PlayEncoder = LabelEncoder()

    Data["Wether"] = WeatherEncoder.fit_transform(Data["Wether"])
    Data["Temperature"] = TemperatureEncoder.fit_transform(Data["Temperature"])
    Data["Play"] = PlayEncoder.fit_transform(Data["Play"])

    print("Encoded Dataset")
    print(Border)
    print(Data)
    print(Border)

    # Features and Label
    X = Data[["Wether","Temperature"]]
    Y = Data["Play"]

    # Step 3 : Train Model
    Model = KNeighborsClassifier(n_neighbors = 3)

    Model.fit(X,Y)

    print("Model trained successfully")
    print(Border)

    # Step 4 : Test Model

    Weather = input("Enter Weather (Sunny / Overcast / Rainy) : ")
    Temperature = input("Enter Temperature (Hot / Mild / Cold) : ")

    Weather = WeatherEncoder.transform([Weather])[0]
    Temperature = TemperatureEncoder.transform([Temperature])[0]

    Prediction = Model.predict([[Weather,Temperature]])

    Result = PlayEncoder.inverse_transform(Prediction)

    print(Border)
    print("Prediction :",Result[0])
    print(Border)

    # Step 5 : Accuracy
    CheckAccuracy(X,Y)

if __name__ == "__main__":
    main()
