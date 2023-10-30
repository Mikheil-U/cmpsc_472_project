import os


def create_process():
    try:
        pid = os.fork()  # Create a new process (child)

        if pid == 0:  # In the child process
            # Replace the current process with a new program (e.g., /bin/ls)
            os.execl('/bin/ls', 'ls', '-l')
        elif pid > 0:  # In the parent process
            print(f"Parent process (PID {os.getpid()}) created a child process (PID {pid}).")
            os.wait()  # Wait for the child process to finish
        else:
            print("Fork failed.")
    except OSError as e:
        print(f"Fork failed: {e}")


def create_process_run():
    create_process()


