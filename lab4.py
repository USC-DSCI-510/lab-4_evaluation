from collections import defaultdict
from typing import List
import os


def generate_frequency_map(file_name: str) -> List:
    with open(file_name, "r") as f:
        lines = f.readlines()
    lines_s = []
    for line in lines:
        lines_s.append(int(line.strip()))
    freq_map = [0 for i in range(10)]
    # print(lines_s)
    for num in lines_s:
        freq_map[num] = freq_map[num] + 1
    return freq_map


def palindrome_finder(file_name: str):
    filename = os.path.basename(file_name)
    palindrome_lines = []
    output_file = open("palindrome_" + filename, "w+")
    with open(file_name, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line)
            words = line.strip().strip('.').split()
            palindrome_line = []
            for word in words:
                if word.lower() == word[::-1].lower() and len(word) > 1:
                    palindrome_line.append(word.lower())
            output_file.write(",".join(palindrome_line) + "\n")
    output_file.close()


def file_extension(file_name: str):
    file_extensions = ['txt', 'doc', 'pdf']
    files_map = defaultdict(list)
    with open(file_name, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            ext_line = line.strip().split(".")[-1]
            if ext_line in file_extensions:
                files_map[ext_line].append(line.strip())
    for ext in file_extensions:
        with open(f"{ext}_{os.path.basename(file_name)}", "w+") as f:
            f.write("\n".join(files_map[ext]))
