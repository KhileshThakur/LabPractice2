array = [6, 4, 8, 2, 9, 7, 3, 1]

def selection_sort(array):
    n = len(array)
    for i in range(0, n):  
        min_idx = i
        for j in range(i+1, n):
            if array[min_idx] > array[j]:
                min_idx = j
        array[min_idx], array[i] = array[i], array[min_idx]
        
        
print("Before : ", array)
selection_sort(array)
print("After : ", array)
