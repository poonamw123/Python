import pandas as pd
import matplotlib.pyplot as plt

def main():
    
    Data = {
        "Name" : ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(Data)
    
    AmitMarks = df[df["Name"] == "Amit"]
    Subjects = ["Math", "Science", "English"]
    Marks =[
        AmitMarks["Math"].values[0], 
        AmitMarks["Science"].values[0], 
        AmitMarks["English"].values[0]
        ]
    
    plt.plot(Subjects, Marks, marker="o")
    
    plt.title("Marks of Amit")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    
    plt.show()
    
    
if __name__ == "__main__":
    main()