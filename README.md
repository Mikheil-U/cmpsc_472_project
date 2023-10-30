# cmpsc_472_project
 Advanced Process Manager with Process Synchronization
# Process Creation and Management with Python

This Python script, `create_process.py`, demonstrates how to create and manage child processes using the `os` module. It provides a simple example of creating a child process and running a different program within it.

## Prerequisites

Before running this script, you should have Python 3.x installed on your system. This code is designed for Unix-like systems.

## Usage

To create and manage child processes, follow these steps:

1. Save the code provided in `create_process.py` on your local system.

2. Open your terminal and navigate to the directory containing the script.

3. Run the script using the following command:

   ```bash
   python create_process.py
   ```

4. The script will create a child process that runs the `/bin/ls` program, listing the contents of the current directory. You will see the output in your terminal.

## Code Explanation

- The script defines a function `create_process()` that creates a child process using `os.fork()`. In the child process, it replaces the current program with a new program (e.g., `/bin/ls`) using `os.execl()`. In the parent process, it waits for the child process to finish using `os.wait()`.

- The `create_process_run()` function is a convenience function that calls `create_process()`.

- The script is designed to run on Unix-like systems, where `fork` and `exec` system calls are available.

## Example Output

When you run the script, you will see output similar to the following:

```
Parent process (PID 12345) created a child process (PID 67890).
```

This output indicates that a child process has been created successfully, and you will see the list of files and directories in the current directory from the child process. The script will wait for the child process to complete before finishing.

## Notes

- This code provides a basic demonstration of process creation and management. In a real-world scenario, you might want to handle errors and implement more advanced process management features.

- This code is not suitable for Windows systems, as it relies on Unix-like system calls. Windows uses different mechanisms for process creation and management.

# Process Management Tool

This Python script, `process_management.py`, is a simple tool for managing processes on your system. It uses the `psutil` library to list running processes, terminate a specific process by its PID, and monitor a process by its PID.

## Prerequisites

Before running this script, you need to have Python 3.x installed on your system, and you should also install the `psutil` library using the following command:

```bash
pip install psutil
```

## Usage

1. Save the code provided in `process_management.py` on your local system.

2. Open your terminal and navigate to the directory containing the script.

3. Run the script using the following command:

   ```bash
   python process_management.py
   ```

4. Follow the on-screen menu to choose one of the following options:

   - List Running Processes: Lists all running processes along with their Process ID (PID), name, Parent PID, and status.
   - Terminate a Process: Enter the PID of a process to terminate it.
   - Monitor a Process: Enter the PID of a process to continuously monitor its status, CPU usage percentage, and memory information.
   - Exit: Quit the tool.

## Features

1. **List Running Processes:**

   The script lists all running processes, providing you with essential information about each process, including its PID, name, parent PID, and status.

2. **Terminate a Process:**

   You can enter the PID of a specific process you want to terminate. The script attempts to terminate the process and provides a confirmation message.

3. **Monitor a Process:**

   By entering the PID of a process, you can continuously monitor its status, CPU usage percentage, and memory information. This option is useful for observing the behavior of specific processes.

## Example Output

When you run the script, you will see a menu allowing you to select the operation you want to perform:

```
Options:
1. List Running Processes
2. Terminate a Process
3. Monitor a Process
4. Exit
Enter your choice:
```

You can interactively select an option by entering the corresponding number. The script will provide you with information and perform the specified operation.

## Notes

- The `psutil` library used in this script provides a straightforward way to manage and monitor processes. Be cautious when terminating processes to avoid affecting system stability.

- This tool is designed for educational and debugging purposes. It's important to use it responsibly, especially when terminating processes.

- This script primarily works on Unix-like systems where `psutil` is supported.


# Multithreading with Mutex

This Python script, `multithreading_with_mutex.py`, demonstrates the use of multithreading with a mutex (lock) for synchronization. It allows you to create and start multiple threads, ensuring that only one thread can access a critical section at a time using a mutex.

## Prerequisites

Before running this script, you should have Python 3.x installed on your system.

## Usage

1. Save the code provided in `multithreading_with_mutex.py` on your local system.

2. Open your terminal and navigate to the directory containing the script.

3. Run the script using the following command:

   ```bash
   python multithreading_with_mutex.py
   ```

4. The script will prompt you to enter the number of threads you want to create and start.

5. Threads will be created and started, each simulating work within a critical section protected by a mutex.

6. The script will wait for all threads to complete before finishing.

## Features

- **Mutex for Synchronization:**

   The script uses Python's `threading.Lock` to create a mutex (lock) for synchronization. This ensures that only one thread can access the critical section at a time.

- **Create and Start Threads:**

   You can specify the number of threads you want to create. The script will create and start the specified number of threads.

## Example Output

When you run the script, you will see the following prompt:

```
Enter the number of threads: 
```

You can input the desired number of threads. Threads will be created and start to simulate work within the critical section. You will see the output indicating which thread is working. The script will wait for all threads to complete before finishing.

## Notes

- Multithreading is used to improve the concurrency of programs. The use of a mutex (lock) is essential for protecting critical sections and avoiding race conditions.

- This script provides a simple example of using a mutex with multiple threads. For more complex scenarios, you may need to implement more advanced synchronization mechanisms and strategies.

- Keep in mind that multithreading can introduce complexity and challenges, and it's important to design and manage your threads carefully to avoid potential issues.

# Inter-Process Communication (IPC) with Sockets

This Python script, `ipc_with_sockets.py`, demonstrates inter-process communication (IPC) using sockets. It allows two separate processes, a server and a client, to communicate over a network socket. The server sends a message, and the client receives and prints the message.

## Prerequisites

Before running this script, you should have Python 3.x installed on your system.

## Usage

1. Save the code provided in `ipc_with_sockets.py` on your local system.

2. Open your terminal and navigate to the directory containing the script.

3. Run the script using the following command:

   ```bash
   python ipc_with_sockets.py
   ```

4. The script will create two separate processes: a server and a client.

5. The server process will establish a socket connection, wait for a client to connect, send a message, and close the connection.

6. The client process will establish a socket connection to the server, receive the message, and print it.

## Features

- **Socket-Based IPC:**

   The script demonstrates IPC using sockets. The server and client communicate over a network socket.

- **Server and Client Processes:**

   Two separate processes, a server and a client, are created. The server sends a message, and the client receives and prints the message.

## Example Output

When you run the script, you will see the following output:

```
Server: Waiting for a connection...
Client received: Hello from the server
```

The server process waits for a connection, and the client process prints the message received from the server.

## Notes

- This script provides a basic example of IPC using sockets. In real-world applications, you can build more complex client-server interactions, including bidirectional communication and handling more significant amounts of data.

- This code is designed for local communication (127.0.0.1). To enable communication over a network, you can specify the IP address and port as needed.

- Be aware that socket-based IPC introduces network-related considerations, such as firewalls, security, and potential network errors.


# Reader-Writer Synchronization

This Python script, `reader_writer_sync.py`, demonstrates reader-writer synchronization using threads. It simulates a scenario where multiple reader and writer threads access a shared resource, ensuring that readers can read simultaneously but only one writer can write at a time.

## Prerequisites

Before running this script, you should have Python 3.x installed on your system.

## Usage

1. Save the code provided in `reader_writer_sync.py` on your local system.

2. Open your terminal and navigate to the directory containing the script.

3. Run the script using the following command:

   ```bash
   python reader_writer_sync.py
   ```

4. The script will create and start multiple reader and writer threads.

5. The reader threads will read the shared resource, and the writer threads will update the resource while adhering to the synchronization constraints.

## Features

- **Reader-Writer Synchronization:**

   The script uses locks (`threading.Lock`) to achieve reader-writer synchronization. Multiple reader threads can read simultaneously, but only one writer thread can write at a time.

- **Multiple Reader and Writer Threads:**

   You can specify the number of reader and writer threads to create and start. The script simulates a situation where multiple threads need to access a shared resource.

## Example Output

When you run the script, you will see output similar to the following:

```
Reader: Resource data
Reader: Resource data
Writer is writing...
Reader: Updated resource data
Reader: Updated resource data
```

This output indicates that multiple reader threads can access and read the shared resource simultaneously. When a writer thread writes to the resource, it ensures that no other threads (readers or writers) can access it during the write operation.

## Notes

- Reader-writer synchronization is essential to avoid race conditions and ensure that data consistency is maintained when multiple threads access shared resources.

- This script provides a basic example of reader-writer synchronization using locks. In real-world scenarios, you may encounter more complex synchronization needs, which may require more advanced synchronization mechanisms.


