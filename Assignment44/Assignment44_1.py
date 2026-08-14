import pandas as pd

def main():
    
    Data = {
        "Name" : ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(Data)
    
    print("DataFrame")
    print("---------------------------------")
    print(df)
    
    print("\nShape of DataFrame")
    print(df.shape)
    
    print("\nColumns")
    print(df.columns)
    
    print("\nData Types")
    print(df.dtypes)
    
if __name__ == "__main__":
    main()