import http.server
import webbrowser

PORT = 8000

server_class = http.server.HTTPServer
handler_class = http.server.CGIHTTPRequestHandler
server_address = ("", PORT)

httpd = server_class(server_address, handler_class)

httpd.serve_forever()