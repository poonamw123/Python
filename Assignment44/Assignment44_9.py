import pandas as pd
import numpy as np

def main():
    
    Data = {
        "Name" : ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan, 76, 88],
        'Science': [91, np.nan, 85]
    }
    df = pd.DataFrame(Data)
    
    print("Original Dataframe")
    print("-------------------------------")
    print(df)
    
    df["Math"] = df["Math"].fillna(df["Math"].mean())
    df["Science"] = df["Science"].fillna(df["Science"].mean())
    
    print("\nDataFrame after filling missing values")
    
    print("--------------------------------")
    
    print(df)
    
    
if __name__ == "__main__":
    main()