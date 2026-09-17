import sys


def save_data() -> None:
    print("\nTransform data:")
    file = open(sys.argv[1], "r")
    lines = file.readlines()
    file.close()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n") + "#\n"
    print("---\n")
    for line in lines:
        print(line, end="")
    print("\n---")

    new_file = input("Enter new file name (or empty): ")
    if new_file == "":
        print("Not saving data")
    else:
        print(f"Saving data to '{new_file}'")
        file = open(new_file, "w")
        for line in lines:
            file.write(line)
        file.close()
        print(f"Data saved in file '{new_file}'")


def print_file_data() -> None:
    print(f"Accessing file: '{sys.argv[1]}'")
    file = open(sys.argv[1])
    content = file.read()
    print("---\n")
    print(content)
    print("---")
    file.close()
    print(f"File '{sys.argv[1]}' closed")


def read_text() -> None:
    try:
        print_file_data()
        save_data()
    except FileNotFoundError as e:
        print(f"[STDERR] Error opening file '{sys.argv[1]}': {e}",
              file=sys.stderr)
    except PermissionError as e:
        print(f"[STDERR] Error opening file '{sys.argv[1]}': {e}",
              file=sys.stderr)
    except KeyboardInterrupt:
        print("\n[STDERR] Error - Keyboard Interrupt", file=sys.stderr)


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) == 2:
        read_text()
    else:
        print(f"[STDERR] Usage: {sys.argv[0]} <file>", file=sys.stderr)
