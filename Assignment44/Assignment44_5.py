import pandas as pd

def main():
    
    Data = {
        "Name" : ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(Data)
    
    df["Name"] = df["Name"].replace("Pooja", "Puja")
    
    print("Updated DataFrame")
    
    print("----------------------------")
    
    print(df)
    
    
if __name__ == "__main__":
    main()