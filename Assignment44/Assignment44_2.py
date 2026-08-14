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
    
    print("\nDescriptive Statistics")
    print("---------------------------------")
    print(df.describe())
    
if __name__ == "__main__":
    main()