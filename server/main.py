import math
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # CPU intensive task
        x = 0
        for i in range(1, 10000):
            x += math.sqrt(i)
        
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"CPU burned successfully!")

if __name__ == "__main__":
    webServer = HTTPServer(("0.0.0.0", 80), SimpleServer)
    print("Server started on port 80.")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
