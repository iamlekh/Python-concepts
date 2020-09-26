import os
from multiprocessing import Process, current_process

def square(number):
    result = number * number
    process_id = os.getpid()    
    print(f'process id : {process_id}')
    print(f'the square of {number} is {result}')

if __name__ == "__main__":
    processes = []
    numbers= [1,2,3,4,5,6,7]
    for num in numbers:
        process = Process(target=square, args=(num,))
        processes.append(process)
        process.start()
