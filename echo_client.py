import socket
import sys


def client(msg, log_buffer=sys.stderr):
    server_address = ('127.0.0.1', 10000)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    client_socket.connect(server_address)
    received_message = ''

    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        client_socket.sendall(msg.encode('utf-8'))
        chunk_size = 16
        size_received = 0
        size_expected = len(msg)
        while True:
            chunk = ''
            chunk = client_socket.recv(chunk_size)
            chunk_decode = chunk.decode('utf8')
            size_received += len(chunk)
            print('received "{0}"'.format(chunk_decode), file=log_buffer)
            received_message += chunk_decode
            if size_received >= size_expected:
                break

    finally:
        print('closing socket', file=log_buffer)
        client_socket.close()
        return received_message


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
