import pandas as pd
import matplotlib.pyplot as plt


def main():
    
    Data = {
        "Name" : ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(Data)
    
    plt.hist(df["Math"], bins = 5)
    
    plt.title("Histogram of Math Marks")
    plt.xlabel("Math Marks")
    plt.ylabel("Frequency")
    
    plt.show()
    
    
if __name__ == "__main__":
    main()