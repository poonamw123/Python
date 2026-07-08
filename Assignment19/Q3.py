from functools import reduce

def main():
    size = int(input("Number of elements : "))
    arr = list()

    print("Input Elements : ")
    for i in range(size):
        arr.append(int(input()))

    filtered_list = list(filter(lambda x: 70 <= x <= 90, arr))
    mapped_list = list(map(lambda x: x + 10, filtered_list))
    
    if mapped_list:
        reduced_val = reduce(lambda a, b: a * b, mapped_list)
    else:
        reduced_val = 0
    
    print(f"List after filter = {filtered_list}")
    print(f"List after map = {mapped_list}")
    print(f"Output of reduce = {reduced_val}")

if __name__ == "__main__":
    main()
