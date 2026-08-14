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
    
    plt.boxplot(df["English"])
    
    plt.title("Boxplot of English Marks")
    plt.ylabel("English Marks")
    
    plt.show()
    
    
if __name__ == "__main__":
    main()