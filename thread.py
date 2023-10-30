import threading

# Mutex for synchronization
mutex = threading.Lock()


# Function that uses the mutex
def thread_work(thread_id):
    with mutex:
        print(f"Thread {thread_id} is working")


# Create and start threads
def create_and_start_threads(num_threads):
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=thread_work, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


def run_thread():
    num_threads = int(input("Enter number of threads"))
    create_and_start_threads(num_threads)


