import pandas as pd
from sklearn.preprocessing import MinMaxScaler


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
    
    Scaler = MinMaxScaler()
    
    df["Math"] = Scaler.fit_transform(df[["Math"]])
    
    print("\nNormalized DataFrame")
    print("-----------------------------------")
    print(df)
    
    
if __name__ == "__main__":
    main()