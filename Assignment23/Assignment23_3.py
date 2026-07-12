import multiprocessing
import os

def EvenCount(No):
    Count = 0

    for i in range(2, No + 1, 2):
        Count = Count + 1

    print("Process ID : ", os.getpid())
    print("Input number : ", No)
    print("Count of Even numbers :  : ", Count)
    print()

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()

    p.map(EvenCount, Data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()