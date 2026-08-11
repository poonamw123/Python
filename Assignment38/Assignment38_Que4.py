import pandas as pd

def main():
    
    Data = pd.read_csv("student_performance_ml.csv")
    
    Result = Data["FinalResult"].value_counts()
    
    print(Result)
    
    PassPercentage = (Result[1] / len(Data)) * 100
    
    FailPercentage = (Result[0] / len(Data)) * 100
    
    print("Percentage of Pass : ", PassPercentage)
    
    print("Percentage of Fail : ", FailPercentage)
    
    print("\nObservation : ")
    print("The dataset contains 60% pass students and 40% fail students.")
    print("The dataset is reasonably balanced because both classes are well represented")
    
if __name__ == "__main__":
    main()
    
    
   