import sys


def save_data() -> None:
    print("---------------------")
    file = open(sys.argv[1], "r+")
    content = file.readline()
    print(f"{content}")
    file.close()


def read_text() -> None:
    try:
        print(f"Accessing file: '{sys.argv[1]}'")
        file = open(sys.argv[1])
        content = file.read()
        print("---\n")
        print(content)
        print("\n---")
        file.close()
        print(f"File {sys.argv[1]} closed")
        save_data()
    except IndexError:
        print(f"Usage: {sys.argv[0]} <file>")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) == 2:
        read_text()
    else:
        print(f"Usage: {sys.argv[0]} <file>")
