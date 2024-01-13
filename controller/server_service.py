from http.server import BaseHTTPRequestHandler, HTTPServer
import db.db_service as db
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

class rest_controller(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/offers':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            offers = db.create_session_and_get_offers()
            offers_json = json.dumps([offer.to_json() for offer in offers])
            self.wfile.write(bytes(offers_json, "utf8"))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes("Not Found", "utf8"))

# Function to start the HTTP server
def start_http_server():
    http_port = int(config.get('server', 'port'))
    http_address = config.get('server', 'address')
    server_address = (http_address, http_port)
    httpd = HTTPServer(server_address, rest_controller)
    print(f"HTTP server started on {server_address }")

    httpd.serve_forever()
