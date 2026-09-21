def secure_archive(
        file_name: str,
        action: str,
        content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "r":
            with open(file_name, action) as file:
                content = file.read()
                return (True, content)
        elif action == "w":
            with open(file_name, action) as file:
                file.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, "Invalid action")
    except Exception as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure archive' to read from a non existent file:")
    print(secure_archive("non/existent/file", "r"))
    print("\nUsing 'secure archive' to read from an inaccesible file:")
    print(secure_archive("/etc/master.passwd", "r"))
    print("\nUsing 'secure archive' to read from a regular file:")
    print(secure_archive("hola.txt", "r"))
    print("\nUsing 'secure archive' to read from a regular file:")
    new_content = "Hola que hace"
    print(secure_archive("prueba1.txt", "w", new_content))
    print("\nUsing 'secure archive' with invalid action:")
    new_content = "Hola muy buenas"
    print(secure_archive("prueba1.txt", "h", new_content))
