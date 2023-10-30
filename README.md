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
