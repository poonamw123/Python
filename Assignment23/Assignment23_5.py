import multiprocessing
import os

def Factorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    print("Process ID : ", os.getpid())
    print("Input number : ", No)
    print("Count of Odd numbers :  : ", Fact)
    print()

def main():
    Data = [10, 15, 20, 25]

    p = multiprocessing.Pool()

    p.map(Factorial, Data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()