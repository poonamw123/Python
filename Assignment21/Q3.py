import threading

# Shared variable
counter = 0

# Lock for synchronization
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

def main():
    threads = []
    # Create 5 threads
    for i in range(5):
        t = threading.Thread(target=increment_counter)
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print(f"Final value of counter: {counter}")

if __name__ == "__main__":
    main()
