# Challenge Session 1: Optimized Bubble Sort
# Problem: Optimize a bubble sort algorithm so that it stops early if the list is already sorted.
# Hint: Use a flag to detect whether a swap occurred.

def bubble_sort_optimized(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

if __name__ == "__main__":
    # Example usage
    data = [5, 1, 4, 2, 8]
    print("Original:", data)
    sorted_data = bubble_sort_optimized(data.copy())
    print("Sorted:", sorted_data)
