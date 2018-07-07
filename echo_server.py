import socket
import sys


def server(log_buffer=sys.stderr):
    address = ('127.0.0.1', 10000)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("making a server on {0}:{1}".format(*address), file=log_buffer)
    server_socket.bind(address)
    server_socket.listen(1)
    chunk_size = 16

    try:
        while True:
            print('waiting for a connection', file=log_buffer)
            conn, addr = server_socket.accept()
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)
                while True:
                    data = conn.recv(chunk_size)
                    if len(data) > 0:
                        print('sent "{0}"'.format(data.decode('utf8')))
                        conn.sendall(data)
                    else:
                        break

            finally:
                print(
                    'echo complete, client connection closed', file=log_buffer
                )
                conn.close()

    except KeyboardInterrupt:
        print('quitting echo server', file=log_buffer)
        server_socket.close()


if __name__ == '__main__':
    server()
    sys.exit(0)
