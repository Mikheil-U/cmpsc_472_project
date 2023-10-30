import ipc
import process_create
import process_manage
import thread
import synchronization

# process_manage.run_process()

if __name__ == '__main__':
    while True:
        choice = int(input('Enter: \n1. Process Creation. \n2. Process Management. \n3. Thread Support. \n4. '
                           'Inter-Process Communication.\n5. Process Synchronization. \n6. Exit Program'))

        if choice == 1:
            process_create.create_process_run()
        elif choice == 2:
            process_manage.run_process()
        elif choice == 3:
            thread.run_thread()
        elif choice == 4:
            ipc.ipc_run()
        elif choice == 5:
            synchronization.synchronization_run()
        elif choice == 6:
            break

