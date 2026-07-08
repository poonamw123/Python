def main():
    size = int(input("Input : Number of elements : "))
    arr = list()

    print("Input Elements : ")
    for i in range(size):
        arr.append(int(input()))

    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        
    print(f"Output : {max_val}")

if __name__ == "__main__":
    main()
