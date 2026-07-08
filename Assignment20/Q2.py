import threading

def even_factor_sum(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:
            total += i
    print(f"Sum of even factors of {num} is {total}")

def odd_factor_sum(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:
            total += i
    print(f"Sum of odd factors of {num} is {total}")

def main():
    num = int(input("Enter an integer number: "))
    
    t1 = threading.Thread(target=even_factor_sum, args=(num,), name="EvenFactor")
    t2 = threading.Thread(target=odd_factor_sum, args=(num,), name="OddFactor")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Exit from main")

if __name__ == "__main__":
    main()
