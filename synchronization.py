import threading

readers = 0
readers_lock = threading.Lock()
writers = 0
writers_lock = threading.Lock()
resource = "Resource data"


def reader():
    global readers
    with readers_lock:
        readers += 1
        if readers == 1:
            writers_lock.acquire()

    print(f"Reader: {resource}")

    with readers_lock:
        readers -= 1
        if readers == 0:
            writers_lock.release()


def writer():
    global writers
    with writers_lock:
        writers += 1

    print("Writer is writing...")
    global resource
    resource = "Updated resource data"

    with writers_lock:
        writers -= 1


def synchronization_run():
    reader_threads = [threading.Thread(target=reader) for _ in range(3)]
    writer_threads = [threading.Thread(target=writer) for _ in range(2)]

    for thread in reader_threads + writer_threads:
        thread.start()

    for thread in reader_threads + writer_threads:
        thread.join()



