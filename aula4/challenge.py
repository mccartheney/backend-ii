# Challenge Session 4: Multiprocessing Sum of Squares
# Problem: Create a multi-process program that divides a large list of numbers into sublists and computes the sum of squares for each sublist concurrently.
# Hint: Use the Pool class from the multiprocessing module.

import multiprocessing

def sum_of_squares(sublist):
    return sum(x * x for x in sublist)

def chunkify(lst, n):
    """Divide lst into n nearly equal chunks."""
    k, m = divmod(len(lst), n)
    return [lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]

if __name__ == "__main__":
    numbers = list(range(1, 10001))  # Large list of numbers
    num_chunks = 4  # Number of processes
    chunks = chunkify(numbers, num_chunks)

    with multiprocessing.Pool(processes=num_chunks) as pool:
        results = pool.map(sum_of_squares, chunks)

    print("Sum of squares for each chunk:", results)
    print("Total sum of squares:", sum(results))
