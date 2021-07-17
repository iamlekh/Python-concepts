from multiprocessing import Process, Queue

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)


def cube(numbers, queue):
    for i in numbers:
        queue.put(i*i*i)


if __name__ == '__main__':

    numbers = range(50)

    queue = Queue()
    square_process = Process(target=square, args=(numbers, queue))
    cube_process = Process(target=cube, args=(numbers, queue))

    square_process.start()
    cube_process.start()

    square_process.join()
    cube_process.join()

    while not queue.empty():
        print(queue.get())