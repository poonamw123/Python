import threading

def print_forward():
    for i in range(1, 51):
        print(f"Thread1: {i}")

def print_backward():
    for i in range(50, 0, -1):
        print(f"Thread2: {i}")

def main():
    t1 = threading.Thread(target=print_forward, name="Thread1")
    t2 = threading.Thread(target=print_backward, name="Thread2")
    
    t1.start()
    t1.join()  # Ensures Thread2 starts only after Thread1 has completed
    
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
