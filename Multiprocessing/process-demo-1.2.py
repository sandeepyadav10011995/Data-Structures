import time
import multiprocessing

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    print(f'Done Sleeping...{seconds}')


processes = []
for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[1])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
# Result : Finished in 1.01 second(s)
