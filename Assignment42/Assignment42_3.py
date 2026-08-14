import math

def MarvellousEuclideanDistance(P1, P2):

    Ans = math.sqrt((P1["StudyHours"] - P2["StudyHours"])**2 +
                    (P1["Attendance"] - P2["Attendance"])**2)

    return Ans

def MarvellousKNN():

    Border = "-" * 40

    Data = [
        {"StudyHours":2, "Attendance":60, "Result":"Fail"},
        {"StudyHours":5, "Attendance":80, "Result":"Pass"},
        {"StudyHours":6, "Attendance":85, "Result":"Pass"},
        {"StudyHours":1, "Attendance":50, "Result":"Fail"}
    ]

    print(Border)
    print("Student Result Prediction using KNN")
    print(Border)

    StudyHours = int(input("Enter Study Hours : "))
    Attendance = int(input("Enter Attendance : "))

    NewStudent = {
        "StudyHours":StudyHours,
        "Attendance":Attendance
    }

    # Calculate Distance
    for Student in Data:
        Student["Distance"] = MarvellousEuclideanDistance(Student, NewStudent)

    # Sort Distance
    SortedData = sorted(Data, key=lambda Item: Item["Distance"])

    # Select K Nearest Neighbours
    K = 3
    Nearest = SortedData[:K]

    print(Border)
    print("Nearest Neighbours")
    print(Border)

    for Student in Nearest:
        print(Student)

    # Majority Voting
    Votes = {}

    for Student in Nearest:

        Label = Student["Result"]

        Votes[Label] = Votes.get(Label, 0) + 1

    Prediction = max(Votes, key=Votes.get)

    print(Border)
    print("Predicted Result :", Prediction)
    print(Border)

def main():

    MarvellousKNN()

if __name__ == "__main__":
    main()
