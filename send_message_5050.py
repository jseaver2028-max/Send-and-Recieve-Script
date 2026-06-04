import socket
import argparse


def send_message(host: str, port: int, message: str) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(message.encode('utf-8'))
        print(f"Sent to {host}:{port}: {message}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send a message over TCP to port 5050')
    parser.add_argument('--host', default='127.0.0.1', help='Target host (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=5050, help='Target port (default: 5050)')
    parser.add_argument('message', help='Message to send')
    args = parser.parse_args()

    send_message(args.host, args.port, args.message)
