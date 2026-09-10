
import multiprocessing

def calculate(number):
    total = 0

    for i in range(1, 5000000):
        total += i * number

    print("CPU calculation finished for:", number)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=calculate, args=(1,))
    p2 = multiprocessing.Process(target=calculate, args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("CPU-intensive multiprocessing completed")