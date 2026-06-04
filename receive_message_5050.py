import socket
import argparse


def receive_messages(host: str, port: int) -> None:
    """Start a TCP server to receive and display messages."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(1)
        print(f"Listening on {host}:{port}...")
        
        try:
            while True:
                conn, addr = sock.accept()
                with conn:
                    print(f"\nConnection from {addr[0]}:{addr[1]}")
                    data = conn.recv(1024)
                    if data:
                        message = data.decode('utf-8')
                        print(f"Payload: {message}")
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Receive messages on port 5050')
    parser.add_argument('--host', default='0.0.0.0', help='Listening host (default: 0.0.0.0, all interfaces)')
    parser.add_argument('--port', type=int, default=5050, help='Listening port (default: 5050)')
    args = parser.parse_args()

    receive_messages(args.host, args.port)
