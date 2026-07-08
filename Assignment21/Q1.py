import threading

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_prime(arr):
    primes = [str(num) for num in arr if is_prime(num)]
    print(f"Prime numbers: {', '.join(primes)}")

def display_non_prime(arr):
    non_primes = [str(num) for num in arr if not is_prime(num)]
    print(f"Non-Prime numbers: {', '.join(non_primes)}")

def main():
    size = int(input("Number of elements: "))
    arr = []
    print("Input Elements:")
    for _ in range(size):
        arr.append(int(input()))
        
    t1 = threading.Thread(target=display_prime, args=(arr,), name="Prime")
    t2 = threading.Thread(target=display_non_prime, args=(arr,), name="NonPrime")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
