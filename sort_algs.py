from utils import find_min

#Swap adjacent elements if they're not in order
#O(N**2) time complexity

def bubble_sort(array):
    for _ in range(len(array)):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

#Set a pivot (Starting at 1)
#Iterate through elements to the left of the pivot, in descending order
#Check if the current element is greater than the pivot
#If it is, move the current element to the right
#Then, move the pivot to the spot where the current element was
#O(N**2) time complexity

def insertion_sort(array):
    pivot = 0

    for i in range(1, len(array)):
        pivot = array[i]

        for j in range(i, -1, -1):
            if array[j] > pivot:
                array[j+1] = array[j]
                array[j] = pivot



#Iterate through each element in the array
#Find the smallest number in i to len(array) range
#Swap the element in i with the smallest number
#O(N**2) time complexity

def selection_sort(array):
    min_pos = 0

    for i in range(len(array)):
        min_pos = find_min(array, i)
        array[i], array[min_pos] = array[min_pos], array[i]
        
        
    
def quick_sort(array, start, end):
    pivot = array[len(array)-1]
    

    i = 0
    j = start+1

    while j <= end-1:
        if pivot > array[j]:
            i += 1
            array[i], array[j] = array[j], array[i]

        j += 1

