def main():
    size = int(input("Input : Number of elements : "))
    arr = list()

    print("Input Elements : ")
    for i in range(size):
        arr.append(int(input()))

    min_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        
    print(f"Output : {min_val}")

if __name__ == "__main__":
    main()
