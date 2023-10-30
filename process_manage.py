import psutil


# List Running Processes
def list_processes():
    for process in psutil.process_iter(attrs=['pid', 'name', 'ppid', 'status']):
        try:
            process_info = process.info
            print(
                f"PID: {process_info['pid']}, Name: {process_info['name']}, Parent PID: {process_info['ppid']}, Status: {process_info['status']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


# Terminate a Process by PID
def terminate_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"Process with PID {pid} terminated.")
    except psutil.NoSuchProcess:
        print(f"Process with PID {pid} not found.")


# Monitor a Process by PID
def monitor_process(pid):
    try:
        process = psutil.Process(pid)
        while True:
            process_info = process.as_dict(attrs=['pid', 'name', 'ppid', 'status', 'cpu_percent', 'memory_info'])
            print(
                f"PID: {process_info['pid']}, Name: {process_info['name']}, Parent PID: {process_info['ppid']}, Status: {process_info['status']}, CPU %: {process_info['cpu_percent']:.2f}, Memory: {process_info['memory_info']}")
    except psutil.NoSuchProcess:
        print(f"Process with PID {pid} not found.")


def run_process():
    while True:
        print("Options:")
        print("1. List Running Processes")
        print("2. Terminate a Process")
        print("3. Monitor a Process")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_processes()
        elif choice == '2':
            pid = int(input("Enter the PID of the process to terminate: "))
            terminate_process(pid)
        elif choice == '3':
            pid = int(input("Enter the PID of the process to monitor: "))
            monitor_process(pid)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

