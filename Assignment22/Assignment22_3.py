from multiprocessing import Pool

def IsPrime(No):
    if No < 2:
        return False
    
    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
        
    return True

def CountPrime(No):
    Count = 0

    for i in range(2, No + 1):
        if IsPrime(i):
            Count += 1

    print("Prime number between 1 and ", No, "=", Count)

    return Count

def main():
    Data = [10000, 20000, 30000, 40000]

    p = Pool()

    Result = p.map(CountPrime, Data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()