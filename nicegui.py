from http.server import BaseHTTPRequestHandler
from nicegui import ui

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body>")
        self.wfile.write(b"<h1>Hello, NiceGUI on Vercel!</h1>")
        self.wfile.write(b"</body></html>")
        return

if __name__ == "__main__":
    ui.run(host="0.0.0.0", port=8080)
