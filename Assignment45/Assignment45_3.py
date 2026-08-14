import pandas as pd


def main():
    
    Data = {
        "Name" : ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82],
        'Gender' : ["Male", "Male", "Female"]
    }
    df = pd.DataFrame(Data)
    
    Result = df.groupby("Gender")[["Math", "Science", "English"]].mean()
    
    print("Average Marks Grouped by Gender")
    
    print("-------------------------------------")
    
    print(Result)
    
    
if __name__ == "__main__":
    main()