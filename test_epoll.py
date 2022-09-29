import select
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('0.0.0.0', 8088))
server_socket.listen(1)
server_socket.setblocking(False)
epoll = select.epoll()

epoll.register(server_socket.fileno(),select.EPOLLIN)

epoll.poll(1)

