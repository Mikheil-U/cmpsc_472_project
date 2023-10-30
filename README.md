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
