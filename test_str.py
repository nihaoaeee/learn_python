import subprocess
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from websocket_server import WebSocketHandler, WebsocketServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open("index.html", "rb") as f:
                self.wfile.write(f.read())
        elif self.path == "/index.html":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open("index.html", "rb") as f:
                self.wfile.write(f.read())
        elif self.path == "/ws":
            WebSocketHandler.handshake(self)


class MyLogger:
    def __init__(self, ws):
        self.ws = ws

    def write(self, message):
        self.ws.send(message)


class MyThread(threading.Thread):
    server = None

    def __init__(self):
        super(MyThread, self).__init__()
        self.daemon = True

    def run(self):
        process = subprocess.Popen(['./test_shell.sh'], stdout=subprocess.PIPE)
        for line in iter(process.stdout.readline, b''):
            message = line.decode().strip()
            for client in self.server.wsmanager.clients.values():
                client.send(message + "\n")


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting server at http://localhost:8000')

    WebsocketServer.handler_class = WebSocketHandler
    ws_server = WebsocketServer("localhost", 8080)
    ws_server.run_forever()
    # logger = MyLogger(ws_server.manager.broadcast)

    MyThread.server = ws_server
    MyThread.start(MyThread())
    httpd.serve_forever()
