import logging
import multiprocessing
import threading

# Configure the logging system
logging.basicConfig(
    level=logging.DEBUG,  # Set the desired log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="process_thread_log.log",  # Log file name
    filemode="w"
)

# Create a logger for the main application
logger = logging.getLogger("Main")


# Function for a process
def process_function():
    logger.info("Process started.")
    # Simulate work
    for _ in range(3):
        logger.debug("Process is working...")
    logger.info("Process finished.")


# Function for a thread
def thread_function():
    logger.info("Thread started.")
    # Simulate work
    for _ in range(3):
        logger.debug("Thread is working...")
    logger.info("Thread finished.")


if __name__ == "__main__":
    logger.info("Application started.")

    # Create a process and a thread
    process = multiprocessing.Process(target=process_function)
    thread = threading.Thread(target=thread_function)

    process.start()
    thread.start()

    process.join()
    thread.join()

    logger.info("Application finished.")
