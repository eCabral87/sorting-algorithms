
def selection_sort(arr):
# Input: arr (1xN)
# Output: sorted arr (1xN)
    pos = 0
    N = len(arr)
    sort_arr = N * [0]
    while pos < N:
        min_val_index = arr.index(min(arr))
        sort_arr[pos] = arr.pop(min_val_index)
        pos += 1
    return sort_arr

def selection_sort_recursive(arr):
# Input: arr (1xN)
# Output: sorted arr (1xN)
    if len(arr) < 2:
        return arr
    else:
        min_val_index = arr.index(min(arr))
        current_val = [arr[min_val_index]]
        arr.pop(min_val_index)
        return current_val + selection_sort_recursive(arr)

if __name__ == "__main__":
    arr = [3, 4, 5, 1, 9, 6, 2, 7, 8]
    print(arr)
    print(selection_sort(arr[:]))
    print(selection_sort_recursive(arr))