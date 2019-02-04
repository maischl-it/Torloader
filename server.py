from http.server import BaseHTTPRequestHandler, HTTPServer

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        text="{\"status\":\"ok\"}"

        print(text)

        # Write content as utf-8 data
        self.wfile.write(bytes(text, "utf8"))

        return None


def startServer(port):
    try:
        server = HTTPServer(('', port), myHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        server.socket.close()

if __name__ == '__main__':
    startServer(9999)