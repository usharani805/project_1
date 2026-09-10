import multiprocessing

def calculate(number):
    total = 0

    for i in range(1000000):
        total = total + i * number

    print("Process completed:", number)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=calculate, args=(1,))
    p2 = multiprocessing.Process(target=calculate, args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All processes completed")