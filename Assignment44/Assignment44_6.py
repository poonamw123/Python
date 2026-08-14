import pandas as pd

def main():
    
    Data = {
        "Name" : ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(Data)
    
    df["Total"] = df["Math"] + df["Science"] + df["English"]
    
    SortedData = df.sort_values(by="Total", ascending=False)

    print("DataFrame sorted by total marks")
    print("--------------------------------------")
    print(SortedData)
    
    
if __name__ == "__main__":
    main()