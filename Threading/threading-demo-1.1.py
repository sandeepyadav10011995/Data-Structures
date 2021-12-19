import time

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done Sleeping...')


for _ in range(10):
    do_something()

finish = time.perf_counter()

# Run Code Concurrently Using the Threading Module
print(f'Finished in {round(finish-start, 2)} second(s)')
# Result : Finished in 10.07 second(s)
