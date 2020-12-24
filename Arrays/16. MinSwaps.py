def minimumSwaps(arr):
    swap_count = 0
    n = len(arr)
    arr_dict = {item: i for i, item in enumerate(arr)}
    checked = [False] * n
    for i in range(n):
        if checked[i] or i == arr_dict[i+1]:
            continue
        cycle_count = 0
        value = i
        while not checked[value]:
            checked[value] = True
            value = arr_dict[value+1]
            cycle_count += 1
        swap_count += cycle_count - 1
    return swap_count

print(minimumSwaps([4, 3, 2, 1]))
