import pandas as pd


def main():
    
    Data = {
        "Name" : ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(Data)
    
    print("Original DataFrame")
    print("----------------------------------")
    print(df)
    
    df = df.drop("English", axis=1)
    
    print("\nDataFrame after dropping English column")
    print("-----------------------------------")
    print(df)
    
    
if __name__ == "__main__":
    main()