import socket


def send_message(host: str, port: int, message: str) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(message.encode('utf-8'))
        print(f"Sent to {host}:{port}: {message}")


if __name__ == '__main__':
    target_host = input("Enter the target ip address: ")
    target_port = 5050

    while True:
        message = input("Enter the message to send (or QUIT to exit): ")
        if message.strip().upper() == 'QUIT':
            print('Exiting sender.')
            break

        if not message.strip():
            message = "Default message"

        send_message(target_host, target_port, message)
