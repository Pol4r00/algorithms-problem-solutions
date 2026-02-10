from sort_algs import bubble_sort
from sort_algs import insertion_sort
from sort_algs import selection_sort
from sort_algs import quick_sort

a1 = [4, 5, 7, 8, 9, 10, 3, 2, 6, 1]
bubble_sort(a1)
print(f"{a1} (Bubble sorted)")

print("-------")

a2 = [5, 3, 2, 2, 9, 1, 7]
insertion_sort(a2)
print(f"{a2} (Insertion sorted)")

print("-------")

a3 = [6, 2, 1, 9, 8, 7]
#selection_sort(a3)
print(f"{a3} (Selection sorted)")

print("-------")

a4 = [8, 2, 4, 7, 1, 3, 9, 6, 5]
quick_sort(a3, 0, len(a3))
print(f"{a3} (Quick sorted)") 

