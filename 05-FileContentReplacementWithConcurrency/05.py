from threading import Thread
from time import perf_counter


def replace(file_name, substr, new_substr):
    print(f"Processing file : {file_name}")
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
    threads = [Thread(target=replace, args=(file_name, "id", "ids")) for file_name in file_names]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    end_time = perf_counter()
    print(f"It took {end_time - start_time} second(s) to complete.")
