#import libraries
import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

#create a static variable to hold PORT
PORT = 8101 # setting to this port number to minimize port conflict

#set handler class into a variable
Handler = http.server.SimpleHTTPRequestHandler

#set types of MIME to be handled

Handler.extensions_map={

			'.manifest': 'text/cache-manifest',
			'.mp3': 'audio/mp4', # serve MP3 MIME
			'.jpg': 'image/jpg', #
			'.mp4': 'video/mp4', # serve Video Content
			'.css': 'text/css',
			'.js': 'application/x-javascript',
			'': 'aplication/octet-stream', #Default
}
#invoke server with parameters to handle MIME and Ports exposure.
httpd = socketserver.TCPServer(("", PORT), Handler)

#prints message to console if server is running
print("server at port", PORT)
#loop inf once server is invoked
httpd.serve_forever()
