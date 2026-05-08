import http.server
import socketserver
import os

PORT = 5000
HOST = "0.0.0.0"

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "":
            self.path = "/musician-reader(33).html"
        return super().do_GET()

    def log_message(self, format, *args):
        pass

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print(f"Serving on http://{HOST}:{PORT}")
    httpd.serve_forever()
