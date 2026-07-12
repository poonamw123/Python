from multiprocessing import Pool
import time

def SumPower(No):
    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + (i ** 5)

    return Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    Start = time.time()

    p = Pool()

    Result = p.map(SumPower, Data)

    p.close()
    p.join()

    End = time.time()

    print("Result : ", Result)
    print("Execution time : ", End - Start)

if __name__ == "__main__":
    main()