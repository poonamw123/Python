from functools import reduce

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    size = int(input("Number of elements : "))
    arr = list()

    print("Input Elements : ")
    for i in range(size):
        arr.append(int(input()))

    filtered_list = list(filter(check_prime, arr))
    mapped_list = list(map(lambda x: x * 2, filtered_list))
    
    if mapped_list:
        reduced_val = reduce(lambda a, b: a if a > b else b, mapped_list)
    else:
        reduced_val = 0
    
    print(f"List after filter = {filtered_list}")
    print(f"List after map = {mapped_list}")
    print(f"Output of reduce = {reduced_val}")

if __name__ == "__main__":
    main()
