import pandas as pd


def main():
    
    Data = {
        "Name" : ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(Data)
    
    df["Gender"] = ["Male", "Male", "Female"]
    print("Original DataFrame")
    print("-----------------------------------")
    print(df)
    
    EncodedData = pd.get_dummies(df, columns=["Gender"])
    
    print("\nDataFrame after One-Hot Encoding")
    print("-----------------------------------")
    print(EncodedData)
    
    
if __name__ == "__main__":
    main()