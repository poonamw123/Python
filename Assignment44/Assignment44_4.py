import pandas as pd

def main():
    
    Data = {
        "Name" : ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(Data)
    
    Result = df[df["Science"] > 85]
    
    print("Students who scored more than 85 in Science")
    print("------------------------------------------------")
    
    print(Result)
    
    
if __name__ == "__main__":
    main()