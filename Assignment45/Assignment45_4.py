import pandas as pd
import matplotlib.pyplot as plt


def main():
    
    Data = {
        "Name" : ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82],
        'Gender' : ["Male", "Male", "Female"]
    }
    df = pd.DataFrame(Data)
    
    Sagar = df[df["Name"] == "Sagar"]
    
    Subjects = ["Math", "Science", "English"]
    
    Marks = [
        Sagar["Math"].values[0],
        Sagar["Science"].values[0],
        Sagar["English"].values[0]
    ]
    
    plt.pie(Marks,
            labels=Subjects,
            autopct="%1.1f%%",
            startangle=90)
    
    plt.title("Subject Marks of Sagar")
    
    plt.show()
    
    
if __name__ == "__main__":
    main()