from http.server import HTTPServer, BaseHTTPRequestHandler

# import argparse


class RequestHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type', 'text/html')
		self.end_headers()
		self.wfile.write('<h1>Deneme</h1>'.encode())


def main():
	# arg_parser = argparse.ArgumentParser(description='Open an HTML file.')
	# arg_parser.add_argument('filename', metavar='filename', type=str, help='Name of the file')

	# args = arg_parser.parse_args()
	# filename = args.filename

	PORT = 8000
	server = HTTPServer(('', PORT), RequestHandler)
	print(f'Server running on port {PORT}')
	server.serve_forever()


if __name__ == '__main__':
	main()
