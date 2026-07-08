import MarvellousNum

def ListPrime(arr):
    total = 0
    for num in arr:
        if MarvellousNum.ChkPrime(num):
            total += num
    return total

def main():
    size = int(input("Input : Number of elements : "))
    arr = list()

    print("Input Elements : ")
    for i in range(size):
        arr.append(int(input()))

    result = ListPrime(arr)
        
    print(f"Output : {result}")

if __name__ == "__main__":
    main()
