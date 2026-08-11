import pandas as pd

def main():
    Data = pd.read_csv("student_performance_ml.csv")
    
    print("------------------- First 5 Records ----------------------")
    print(Data.head())
    
    print("\n------------------ Last 5 Records ---------------")
    print(Data.tail())
    
    print("\n------------------ Shape of Dataset -------------")
    print("Total Rows : ", Data.shape[0])
    print("Total Columns : ", Data.shape[1])
    
    print("\n------------------ Column Names ----------------")
    print(Data.columns.tolist())
    
    print("\n------------------ Data Types ------------------")
    print(Data.dtypes)
    
if __name__ == "__main__":
    main()