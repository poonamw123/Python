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
    
    df["Total"] = df["Math"] + df["Science"] + df["English"]
    
    df["Status"] = df["Total"].apply(lambda Marks: "Pass" if Marks >= 250 else "Fail")
    
    PassCount = (df["Status"] == "Pass").sum()
    
    print("Student Result")
    
    print("----------------------------------------")
    
    print(df)
    
    print("----------------------------------------")
    print("Number of students passed : ", PassCount)
    
    
if __name__ == "__main__":
    main()