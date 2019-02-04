from http.server import BaseHTTPRequestHandler, HTTPServer

print("Nicht direkt aufrufen")

text=""

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Write content as utf-8 data
        self.wfile.write(bytes(text, "utf8"))

        return None


def startServer(strText,port):
    global text

    text=strText

    try:
        server = HTTPServer(('', port), myHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        server.socket.close()
