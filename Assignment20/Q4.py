import threading

def count_small(text):
    count = sum(1 for c in text if c.islower())
    t = threading.current_thread()
    print(f"Thread Name: {t.name}, Thread ID: {t.ident} -> Lowercase count: {count}")

def count_capital(text):
    count = sum(1 for c in text if c.isupper())
    t = threading.current_thread()
    print(f"Thread Name: {t.name}, Thread ID: {t.ident} -> Uppercase count: {count}")

def count_digits(text):
    count = sum(1 for c in text if c.isdigit())
    t = threading.current_thread()
    print(f"Thread Name: {t.name}, Thread ID: {t.ident} -> Digits count: {count}")

def main():
    text = input("Enter a string: ")
    
    t1 = threading.Thread(target=count_small, args=(text,), name="Small")
    t2 = threading.Thread(target=count_capital, args=(text,), name="Capital")
    t3 = threading.Thread(target=count_digits, args=(text,), name="Digits")
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
