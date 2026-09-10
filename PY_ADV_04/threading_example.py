import threading

def print_message(message):
    print(message)

thread1 = threading.Thread(
    target=print_message,
    args=("Hello from Thread 1",)
)

thread2 = threading.Thread(
    target=print_message,
    args=("Hello from Thread 2",)
)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All threads completed")