def find_min(array, start=0):
    min_pos = start

    for i in range(start, len(array)):
        if array[i] < array[min_pos]:
            min_pos = i
            

    return min_pos
