import threading

def display_maximum(arr):
    if arr:
        print(f"Maximum element: {max(arr)}")
    else:
        print("Maximum element: None")

def display_minimum(arr):
    if arr:
        print(f"Minimum element: {min(arr)}")
    else:
        print("Minimum element: None")

def main():
    size = int(input("Number of elements: "))
    arr = []
    print("Input Elements:")
    for _ in range(size):
        arr.append(int(input()))
        
    t1 = threading.Thread(target=display_maximum, args=(arr,))
    t2 = threading.Thread(target=display_minimum, args=(arr,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
