import socket


def send_message(host: str, port: int, message: str) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(message.encode('utf-8'))
        print(f"Sent to {host}:{port}: {message}")


if __name__ == '__main__':
    target_host = '192.168.1.11'#Changes the ip address you are sending stuff to
    target_port = 5050#Changes the port you are sending stuff to
    message = 'Hello World'#Changes the message you are sending

    send_message(target_host, target_port, message)
