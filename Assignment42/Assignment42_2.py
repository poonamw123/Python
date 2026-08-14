import math

def MarvellousEucDistance(P1, P2):
    Ans = math.sqrt((P1["X"] - P2["X"])**2 + (P1["Y"] - P2["Y"])**2)
    return Ans

def PredictClass(SortedData, K):

    Nearest = SortedData[:K]

    Votes = {}

    for Neighbour in Nearest:
        Label = Neighbour["label"]
        Votes[Label] = Votes.get(Label, 0) + 1

    Prediction = max(Votes, key=Votes.get)

    print("K =", K, "->", Prediction)

def MarvellousKNNClassifier():

    Border = "-" * 40

    Data = [
        {"point":"A","X":1,"Y":2,"label":"Red"},
        {"point":"B","X":2,"Y":3,"label":"Red"},
        {"point":"C","X":3,"Y":1,"label":"Blue"},
        {"point":"D","X":6,"Y":5,"label":"Blue"},
        {"point":"E","X":5,"Y":4,"label":"Blue"}
    ]

    print(Border)
    print("Marvellous KNN Classifier")
    print(Border)

    NewPoint = {"X":2,"Y":2}

    print("New Point :", NewPoint)

    for d in Data:
        d["distance"] = MarvellousEucDistance(d, NewPoint)

    SortedData = sorted(Data, key=lambda Item: Item["distance"])

    print(Border)
    print("Sorted Data")
    print(Border)

    for d in SortedData:
        print(d)

    print(Border)
    print("Prediction Results")
    print(Border)

    PredictClass(SortedData, 1)
    PredictClass(SortedData, 3)
    PredictClass(SortedData, 5)

    print(Border)
    print("Observation")
    print(Border)
    print("As the value of K increases, more neighbours participate")
    print("in voting. Therefore, the predicted class may change")
    print("depending on the majority of the nearest neighbours.")

def main():
    MarvellousKNNClassifier()

if __name__ == "__main__":
    main()