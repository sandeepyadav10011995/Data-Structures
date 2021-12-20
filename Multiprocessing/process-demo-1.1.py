import time

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done Sleeping...')


do_something()

finish = time.perf_counter()

# Run Code in Parallel Using the Multiprocessing Module
print(f'Finished in {round(finish-start, 2)} second(s)')
# Result : Finished in 1.01 second(s)
