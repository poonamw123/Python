import threading

def print_even():
    count = 0
    num = 2
    while count < 10:
        print(f"Even: {num}")
        num += 2
        count += 1

def print_odd():
    count = 0
    num = 1
    while count < 10:
        print(f"Odd: {num}")
        num += 2
        count += 1

def main():
    t1 = threading.Thread(target=print_even, name="Even")
    t2 = threading.Thread(target=print_odd, name="Odd")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
