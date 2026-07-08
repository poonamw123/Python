def main():
    size = int(input("Input : Number of elements : "))
    arr = list()

    print("Input Elements : ")
    for i in range(size):
        arr.append(int(input()))

    total = 0
    for num in arr:
        total += num
        
    print(f"Output : {total}")

if __name__ == "__main__":
    main()
