# Challenge Session 3: Multi-threaded File Downloader
# Problem: Create a multi-threaded program that downloads multiple files concurrently from given URLs.
# Hint: Use the threading module along with urllib.request.urlretrieve.

import threading
import urllib.request

def download_file(url, filename):
    print(f"Starting download: {url}")
    urllib.request.urlretrieve(url, filename)
    print(f"Finished download: {filename}")

def download_files_concurrently(urls):
    threads = []
    for i, url in enumerate(urls):
        filename = f"file_{i+1}"
        thread = threading.Thread(target=download_file, args=(url, filename))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Example URLs (replace with real downloadable files for actual use)
    urls = [
        "https://www.example.com/file1.txt",
        "https://www.example.com/file2.txt",
        "https://www.example.com/file3.txt"
    ]
    download_files_concurrently(urls)
