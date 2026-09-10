import threading

def count():
    total = 0

    for i in range(1000000):
        total += i

    print("Finished")

thread1 = threading.Thread(target=count)
thread2 = threading.Thread(target=count)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads completed")