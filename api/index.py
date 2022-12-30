from http.server import BaseHTTPRequestHandler

import trafilatura


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Get the URL from the query string
        url = self.path[1:]

        text = trafilatura.extract(url, output_format="json")

        self.send_response(200)

        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(text.encode("utf-8"))
