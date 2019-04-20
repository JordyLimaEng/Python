from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        arq = open('Config.txt', 'r')
        texto = arq.read()
        arq.close()
        json_str = json.dumps(texto)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json_str.encode(encoding='utf_8'))

    def do_POST(self):
        arq = open('Config.txt', 'r')
        texto = arq.read()
        arq.close()
        json_str = json.dumps(texto)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json_str.encode(encoding='utf_8'))
        

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()