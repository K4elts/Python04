import sys

if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    try:
        print(f"Accessing file: {sys.argv[1]}")
        file = open(sys.argv[1])
        content = file.read()
        print("---\n")
        print(content)
        print("\n---")
        file.close()
        print(f"File {sys.argv[1]} closed")
    except IndexError:
        print(f"Usage: {sys.argv[0]} <file>")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
