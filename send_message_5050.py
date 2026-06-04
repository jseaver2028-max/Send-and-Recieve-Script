import socket


def send_message(host: str, port: int, message: str) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(message.encode('utf-8'))
        print(f"Sent to {host}:{port}: {message}")


if __name__ == '__main__':
    target_host = '192.168.1.11'
    target_port = 5050
    message = 'Hello World'

    send_message(target_host, target_port, message)
