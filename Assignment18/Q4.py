def main():
    size = int(input("Input : Number of elements : "))
    arr = list()

    print("Input Elements : ")
    for i in range(size):
        arr.append(int(input()))

    search_element = int(input("Element to search : "))
    
    count = 0
    for num in arr:
        if num == search_element:
            count += 1
        
    print(f"Output : {count}")

if __name__ == "__main__":
    main()
