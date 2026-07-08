import threading

def even_list_sum(arr):
    total = sum(x for x in arr if x % 2 == 0)
    print(f"Sum of even elements: {total}")

def odd_list_sum(arr):
    total = sum(x for x in arr if x % 2 != 0)
    print(f"Sum of odd elements: {total}")

def main():
    size = int(input("Number of elements: "))
    arr = []
    print("Input Elements:")
    for _ in range(size):
        arr.append(int(input()))
        
    t1 = threading.Thread(target=even_list_sum, args=(arr,), name="EvenList")
    t2 = threading.Thread(target=odd_list_sum, args=(arr,), name="OddList")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
