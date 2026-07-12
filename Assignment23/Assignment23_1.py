import multiprocessing
import os

def EvenSum(No):
    Sum = 0

    for i in range(2, No + 1, 2):
        Sum = Sum + i

    print("Process ID : ", os.getpid())

    print("Input number : ", No)

    print("Sum of even numbers : ", Sum)

    print()

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()

    p.map(EvenSum, Data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()