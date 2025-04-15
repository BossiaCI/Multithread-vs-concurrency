import threading
import time
import random

def download_file(filename):
    print(f"Starting download: {filename}")
    # Simulate a download time between 1 and 5 seconds
    download_time = random.randint(1,5)
    time.sleep(download_time)
    print(f"Finished download: {filename} (took {download_time} seconds)")



if __name__  == "__main__":
    # List of files to download
    files_to_download = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]

    threads = []

    # Create and start a thread for each file download
    for file in files_to_download:
        t = threading.Thread(target=download_file, args=(file,))
        t.start()
        threads.append(t)

    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    print("All downloads completed !")