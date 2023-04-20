import os
import threading
import time
import csv


def convert_file_to_uppercase(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as f:
            file_content = f.read()
        with open(output_file_path, 'w') as f:
            f.write(file_content.upper())
    except Exception as e:
        print(f"Error in thread {threading.current_thread().name}: {e}")


def worker(input_dir_path, output_dir_path, files_to_process):
    for filename in files_to_process:
        input_file_path = os.path.join(input_dir_path, filename)
        output_file_path = os.path.join(output_dir_path, filename)
        convert_file_to_uppercase(input_file_path, output_file_path)


def convert_files_in_directory_to_uppercase(input_dir_path, output_dir_path, n, t):
    files_to_process = [f"file{i}.txt" for i in range(n)]
    chunk_size = n // t
    threads = []

    for i in range(t):
        start = i * chunk_size
        end = n if i == t - 1 else (i + 1) * chunk_size
        thread_files = files_to_process[start:end]
        thread = threading.Thread(target=worker, args=(
            input_dir_path, output_dir_path, thread_files))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


params = [
    (10, 1), (10, 2), (10, 3), (10, 4),
    (20, 1), (20, 2), (20, 3), (20, 4)
]

input_path = os.path.join("input")
output_path = os.path.join("output")

time_taken_dict = {}
for n, t in params:
    start_time = time.time()
    convert_files_in_directory_to_uppercase(input_path, output_path, n, t)
    time_taken = time.time() - start_time
    time_taken_dict[(n, t)] = f"{time_taken:.2f}"
    print(f"Time taken for n={n}, t={t}: {time_taken:.2f} seconds")

with open('time_taken.csv', 'w', newline='') as csvfile:
    fieldnames = ['n', 't=1', 't=2', 't=3', 't=4']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
        'n': 10,
        't=1': time_taken_dict[(10, 1)],
        't=2': time_taken_dict[(10, 2)],
        't=3': time_taken_dict[(10, 3)],
        't=4': time_taken_dict[(10, 4)]
    })
    writer.writerow({
        'n': 20,
        't=1': time_taken_dict[(20, 1)],
        't=2': time_taken_dict[(20, 2)],
        't=3': time_taken_dict[(20, 3)],
        't=4': time_taken_dict[(20, 4)]
    })
