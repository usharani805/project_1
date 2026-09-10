import threading

def task(name):
    print("Hello from", name)

thread1 = threading.Thread(target=task, args=("Thread 1",))
thread2 = threading.Thread(target=task, args=("Thread 2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All threads completed")