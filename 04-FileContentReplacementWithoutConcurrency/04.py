from time import perf_counter

def replace(file_name, substr, new_substr):
    print(f"Processing the file: {file_name}")
    with open(file_name, "r") as f:
        content = f.read()
    content = content.replace(substr, new_substr)
    with open(file_name, "w") as f:
        f.write(content)

def main():
    file_names = [
        "text_files/1.txt",
        "text_files/2.txt",
        "text_files/3.txt",
        "text_files/4.txt",
        "text_files/5.txt",
        "text_files/6.txt",
        "text_files/7.txt",
        "text_files/8.txt",
        "text_files/9.txt",
        "text_files/10.txt",
    ]
    for file_name in file_names:
        replace(file_name, 'id', 'ids')

if __name__ == "__main__":
    start_time = perf_counter()
    main()
    end_time = perf_counter()
    print(f"It took {end_time - start_time: 0.6f} second(s) to complete.")