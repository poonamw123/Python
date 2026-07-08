import threading
from functools import reduce

def compute_sum(arr, results):
    results['sum'] = sum(arr)

def compute_product(arr, results):
    if arr:
        results['product'] = reduce(lambda x, y: x * y, arr)
    else:
        results['product'] = 1

def main():
    size = int(input("Number of elements: "))
    arr = []
    print("Input Elements:")
    for _ in range(size):
        arr.append(int(input()))
        
    results = {}
    
    t1 = threading.Thread(target=compute_sum, args=(arr, results))
    t2 = threading.Thread(target=compute_product, args=(arr, results))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    # Returning the results to main thread and displaying them
    print(f"Sum of elements: {results.get('sum')}")
    print(f"Product of elements: {results.get('product')}")

if __name__ == "__main__":
    main()
